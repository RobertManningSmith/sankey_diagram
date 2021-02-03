from matplotlib.sankey import Sankey
from matplotlib import pyplot as plt

# first flow into the diagram, the first value is the total quantity introduced into the
# flow, the remaining, the subsequent terms remove a certain quantity from the first flow.

# In this example we will plot the percent health care budget consumed by various conditions, 50% is spent on HIV, 30%
# on road traffic injuries and 20% on epilepsy, we store this information in two arrays, flows1 which houses the
# data and labels1 which gives each percentage a label.

# I want the total budget to go in a straight line from left to right, the hiv budget to go up from the total budget,
# the road traffic budget to carry on straight and the epilepsy budget to go down, I will store these directions in an
# array orientations1, the first entry is 0 as we don't want to change the orientations from the default direction,
# the second entry is 1 as we want the HIV budget to go up, the third entry is 0 as we want the entry to go on straight,
# the fourth entry is -1 as we want the epilepsy budget to go down.
flow1 = [100, -30, -50, -20]
labels1 = ['Total expenditure on health', '% spent on HIV', "% spent on road "
                                                            "\n"
                                                            "traffic injuries",
           '% spent on epilepsy']
orientations1 = [0, 1, 0, -1]
# The second flow breaks down the what the road traffic injuries budget was spent on, 10% of
# the total budget was spent on bandages, 15% on plaster of paris and 5% on surgery, we store data in flows 2 and the
# labelling info in labels2, leaving the first entry blank as this is where the '% spent on road traffic injuries'
# flow links to the breakdown flow.
# In the orientations, the first entry is zero as we want this flow to carry on in the same direction, the second entry
# for bandage expenditure is 1 as we want this to head up from the flow, the second entry is zero as we want the
# plaster of paris expenditure to go on straight and finally the fourth entry is -1 to make the surgery expenditure go
# down
flow2 = [50, -10, -15, -25]
labels2 = ['', 'bandages', 'plaster of paris', 'surgery']
orientations2 = [0, 1, 0, -1]

# Now we have created the flows and set the labels and directions the arrows go in, we can create the sankey diagram.

# The sankey object needs to be scaled (controls how much space the diagram takes up), but if it's not scaled properly
# it can look pretty terrible, I found that a fairly reasonable scale to use is to use 1/a where a is the first entry of
# the first flow (in this example 100).
# The offset zooms into and out from the diagram

fig = plt.figure(figsize=(20, 10))  # create figure
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[])
ax.axis('off')  # Turn off the box for the plot
plt.title('Budget example')  # create title
sankey = Sankey(ax=ax,
                scale=1 / flow1[0],
                offset=0.2,
                unit='')  # create sankey object
sankey.add(flows=flow1,  # add the first flow
           labels=labels1,
           orientations=orientations1,
           pathlengths=[0.1, 0.1, 0.1, 0.1],
           trunklength=0.605,  # how long this flow is
           edgecolor='#027368',  # choose colour
           facecolor='#027368')
sankey.add(flows=flow2,
           labels=labels2,
           trunklength=0.5,
           pathlengths=[0.25, 0.25, 0.25, 0.25],
           orientations=[0, 1, 0, -1],
           prior=0,  # which sankey are you connecting to (0-indexed)
           connect=(2, 0),  # flow number to connect: this is the index of road traffic injury portion of the budget in
           # the first flow (third entry, python index 2) which connects to the first entry in the second flow (python
           # index 0).
           edgecolor='#58A4B0',  # choose colour
           facecolor='#58A4B0')
diagrams = sankey.finish()
plt.savefig('sankey_example.png', dpi=600)
plt.show()
plt.close()
