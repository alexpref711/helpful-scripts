from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# Re-works the data frame to make the analysis easier
# In the future this would be a separate function to output a new df, this way all the cols have names!
plt.style.use('seaborn-muted')
INPUT = r"C:\Users\Alexandre\Desktop\Budisa lab\Projects\22-04-01__FlpEvo\F-Pro_Evolution_4\ALE_short_double_mutant.csv"
raw = pd.read_csv(INPUT)
df = raw.transpose()

"""It is best to copy into each final destination for simple retuning"""
neg = df.iloc[0:2].mean()
neg_std = df.iloc[0:2].std()
limit = df.iloc[2:4].mean()
limit_std = df.iloc[2:4].std()
pos = df.iloc[4:6].mean()
pos_std = df.iloc[4:6].std()

r_flp = df.iloc[6:10].mean()
r_std = df.iloc[6:10].std()

s_flp = df.iloc[10:15].mean()
s_std = df.iloc[10:15].std()

mix_flp = ''
mix_std = ''
# Problems, the labelling is messed cause agg have no name
def make_cols(chart_label, array, *args, **kwargs,):
    """
    :param chart_label: The label for the chart as string
    :param array: Growth values to plot
    :param args: Growth values for overlay
    :param std: Optional standard dev for the main values
    :return: Auto saves to global OUTPUT
    """
    x_vals = np.arange(1, len(array) + 1)  # Adjust the increment for public
    fig, ax = plt.subplots()
    # Now it is time to work
    if kwargs:
        ax.bar(x_vals, array, color='#93CAED', yerr=kwargs['std'])  # Main set of bars
    else:
        ax.bar(x_vals, array, color='#93CAED')
    if args:
        ax.bar(x_vals, args[0], color='#F47174', label="Limiting Control")   # Optional overlay

    # Formatting, need to set the labels and the ticks
    ax.set_title(chart_label, fontsize=18)
    ax.set_ybound(lower=0, upper=1.5)  # Needs to be changed be hand for the positive controls!
    ax.set_xlabel("Days of Growth", fontsize=15)
    ax.set_ylabel("OD 600", fontsize=15)
    plt.savefig(chart_label)

# Would be better is it took the limit as a kwarg
def make_lines(chart_label, array1, *args):
    x_vals = np.arange(1, len(array1) + 1)  # Adjust the increment for public viewing
    fig, ax = plt.subplots()
    ax.plot(x_vals, array1, label=array1.name)
    if len(args) >= 1:
        ax.plot(x_vals, args[0], label=args[0].name)
    if len(args) == 2:
        ax.plot(x_vals, args[1], label=args[1].name)

    # Formatting
    ax.set_title(chart_label, fontsize=18)
    ax.set_ybound(lower=0, upper=1.5)  # Needs to be changed be hand for the positive controls!
    ax.set_xlabel("Days of Growth", fontsize=15)
    ax.set_ylabel("OD 600", fontsize=15)
    # plt.legend()
    plt.savefig(chart_label)

def make_line_48():
    pass

make_cols('4R-Fluoroproline', r_flp, limit, std=r_std)
make_cols('4S-Fluoroproline', s_flp, limit, std=s_std)
# make_cols('Mixed Fluoroprolines', mix_flp, limit, std=mix_std)

make_lines('4R-Flp', r_flp, limit)
make_lines('4S-Flp', s_flp, limit)
# make_lines('M-Flp', mix_flp, limit)
# make_lines('S-Flp and Mixed-Flp', s_flp, mix_flp, limit)
