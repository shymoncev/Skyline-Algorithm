import numpy as np
import pandas as pd
import matplotlib as plt


class PointsDataFrame:
    def __init__(
            self,
            datas: np.ndarray[np.ndarray[int | float]] = None,
            low: int = 10,
            high: int | None = 1000,
            size: tuple[int, int] = (10, 2),
            random_seed: int | None = None
            ) -> None:
        column = ['x', 'y', 'z', 'w']
        if datas is not None:
            df = pd.DataFrame(datas, columns=column[:datas.shape[1]])
            df['partition'] = ''
        else:
            if random_seed:
                np.random.seed(random_seed)
            df = pd.DataFrame(
                np.random.randint(low, high, size=size),
                columns=column[:size[1]],
                index=None
                )
            df['partition'] = ''
        self.df = df

    def show_points(self):
        if len(self.df.columns) > 3:
            print(f'The dimention({len(self.df.columns)}) of data > 3')
        else:
            if len(self.df.columns) == 2:
                plt.scatter(data=self.df, x='x', y='y', color='black')
                plt.show()
            else:
                fig = plt.figure(figsize=(9, 6))
                ax = fig.add_subplot(111, projection='3d')
                x = self.df.x
                y = self.df.y
                z = self.df.z
                ax.scatter(x, y, z, color='black', alpha=0.5)
