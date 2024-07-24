import numpy as np
import pandas as pd
from src.jobs.checker import check


def _divide(df):
    medians = dict()
    for column in df.columns[:-1]:
        medians[column] = np.mean(df[column].values)
    part0 = pd.DataFrame(
        df[(df['x'] > medians['x']) & (df['y'] > medians['y'])]
        )
    part1 = pd.DataFrame(
        df[(df['x'] <= medians['x']) & (df['y'] > medians['y'])]
        )
    part2 = pd.DataFrame(
        df[(df['x'] <= medians['x']) & (df['y'] <= medians['y'])]
        )
    part3 = pd.DataFrame(
        df[(df['x'] > medians['x']) & (df['y'] <= medians['y'])]
        )

    part0['partition'] = part0['partition'] + '0'
    part1['partition'] = part1['partition'] + '1'
    part2['partition'] = part2['partition'] + '2'
    part3['partition'] = part3['partition'] + '3'

    part_df = pd.concat([part0, part1, part2, part3], ignore_index=True)
    return part_df


def _divide_all(part_df):
    while checker := check(part_df):
        for part in checker:
            df = part_df[part_df['partition'] == part]
            part_df.drop(df.index, axis=0, inplace=True)
            part_df = pd.concat([_divide(df), part_df], ignore_index=True)
    part_df['group'] = [index[:-1] for index in part_df['partition'].values]
    return part_df


def _dominates(p1, p2):
    return all(x <= y for x, y in zip(p1, p2)) and any(x < y for x, y in zip(p1, p2))


def divide_and_conquer(df):
    point_df = _divide_all(_divide(df))
    while True:
        before = len(point_df)

        for index in point_df['group'].value_counts().index:
            if len(index) == 0:
                continue

            group = point_df[point_df['group'] == index]
            indices = list(group.index)

            for i in indices:
                for j in indices:
                    if i != j:
                        if _dominates(
                            group.loc[i][['x', 'y']].values,
                            group.loc[j][['x', 'y']].values
                        ):
                            point_df.drop([j], inplace=True)
                            indices.remove(j)

            point_df.loc[indices, 'partition'] = \
                point_df.loc[indices]['group'].values
            point_df.loc[indices, 'group'] = \
                [index[:-1] for index in point_df.loc[indices]['group'].values]

        after = len(point_df)

        if after == before:
            break

    point_df.drop(point_df[point_df['partition'] == '0'].index, inplace=True)

    last = [list(point) for point in list(point_df[['x', 'y']].values)]
    remove_list = list()
    for p in last:
        for q in last:
            if p != q:
                if _dominates(p, q):
                    remove_list.append(q)
    for p in remove_list:
        try:
            last.remove(p)
        except ValueError:
            pass
    return last
