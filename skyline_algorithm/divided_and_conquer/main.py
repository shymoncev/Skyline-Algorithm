import matplotlib.pyplot as plt
from src.data.point import PointsDataFrame
from src.jobs.dnc_module import divide, divide_and_conquer, divide_all


def main():
    points = PointsDataFrame(size=(1000, 2), random_seed=42)
    df = points.df

    points_df = divide_all(divide(df))
    skyline = divide_and_conquer(points_df)

    plt.scatter(
        x=[data[0] for data in df[['x', 'y']].values],
        y=[data[1] for data in df[['x', 'y']].values],
        s=3
        )
    plt.scatter(
        x=[data[0] for data in skyline],
        y=[data[1] for data in skyline]
        )
    plt.show()


if __name__ == '__main__':
    main()
