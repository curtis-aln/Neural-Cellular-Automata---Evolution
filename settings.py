import numpy as np

""" pygame parameters """
WINDOW_COLOR = (0, 0, 0)
WINDOW_TITLE = "Evolved Automata"
WINDOW_DIMS = (1550, 850)
MAX_FRAME_RATE = 600

""" cellular automata parameters """
AUTOMATA_DEPTH = 4 # the amount of third dimensional layers per sim
TICKS_PER_GEN = 100 # frames every generation
ANALYZE_INDEX = 0  # index used to calculate score
PARRELEL_SIMULATIONS = 200

""" evolution settings """
B_MUTATION_RATE  = 15#%
B_MUTATION_RANGE = 15#%
W_MUTATION_RATE  = 15#%
W_MUTATION_RANGE = 15#%

UNMUTATED_PERCENT   = 10 # percent of the population that go mutated
UNDISCARDED_PERCENT = 50 # percent of the population that isn't discarded

L1_W_RANGE = 0.04 # range of weight values allowed to initilise layer 1
L2_W_RANGE = 0.04 # range of weight values allowed to initilise layer 2
L1_B_RANGE = 0.0 # range of bias values allowed to initilise layer 1
L2_B_RANGE = 0.0 # range of bias values allowed to initilise layer 2

SOBEL_X = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])
SOBEL_Y = SOBEL_X.T

SOBEL_Z = np.array([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
])

# making them 3d matricies
SOBEL_X = np.transpose(SOBEL_X[None,:, :], (1, 2, 0))
SOBEL_Y = np.transpose(SOBEL_Y[None,:, :], (1, 2, 0))