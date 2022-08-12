# parameters and paths
PROJECT_FOLDER = "/datadisk/Dropbox/fromPapers/Schaworonkow_2021_biorxiv/eeg-leadfield-mixing"
EEG_DATA_FOLDER = f"{PROJECT_FOLDER}/eeg_lemon/"
MEG_DATA_FOLDER = f"{PROJECT_FOLDER}/meg_schoffelen/"
FIG_FOLDER = f"{PROJECT_FOLDER}/figures/"
CSV_FOLDER = f"{PROJECT_FOLDER}/csv/"
RESULTS_FOLDER = f"{PROJECT_FOLDER}/results/"
LEADFIELD_DIR = f"{PROJECT_FOLDER}/leadfields/"


# spectral parametrization
SPEC_PARAM_DIR_EEG = f"{RESULTS_FOLDER}/eeg/spec_param/"
SPEC_PARAM_DIR_MEG = f"{RESULTS_FOLDER}/meg/spec_param/"

SPEC_PARAM_CSV_EEG = f"{RESULTS_FOLDER}/eeg_center_frequencies.csv"
SPEC_PARAM_CSV_MEG = f"{RESULTS_FOLDER}/meg_center_frequencies.csv"

ALPHA_FMIN = 8
ALPHA_FMAX = 13
SPEC_FMIN = 2
SPEC_FMAX = 35
SPEC_NR_PEAKS = 5
SPEC_NR_SECONDS = 2
SNR_THRESHOLD = 0.5

# SSD
SSD_BANDWIDTH = 2
SSD_NR_COMPONENTS = 10
SSD_EEG_DIR = f"{RESULTS_FOLDER}/eeg/ssd/"
SSD_MEG_DIR = f"{RESULTS_FOLDER}/meg/ssd/"

# patterns
PATTERN_EEG_DIR = f"{RESULTS_FOLDER}/eeg/patterns/"
PATTERN_MEG_DIR = f"{RESULTS_FOLDER}/meg/patterns/"
