import VoigtFit
import scipy.constants
import numpy as np

data_file = 'M83-POS1_HI_1215_lsf_mask_testerrors.reg'
lsf_file = 'M83_POS1_COS_LSF_TOTAL_G130M_1291_LP1.dat'

target = 'M83-POS1'
z_sys = 0.

ion = 'HI_1215'

dataset = VoigtFit.DataSet(z_sys)

### Name output file
dataset.set_name(target)


# -- Load Data and input to the dataset
wl, flux, err,mask = np.loadtxt(data_file, usecols=(0,1,2,4), unpack=True)

dataset.add_data(wl, flux,err=err,mask=mask, res=lsf_file, nsub=6,
                 normalized=True)

# -- Specify the line to be analyzed
dataset.add_line(ion, velspan=15000)


#--- Add components
#                               ion     z   b     logN
dataset.add_component_velocity('HI',12.8, 0.5, 20.57, var_N=False,var_z=False, var_b=False)
dataset.add_component_velocity('HI', 422., 0.5,19.9, var_z=False, var_b=False)

# -- And fit the dataset
dataset.prepare_dataset(norm=True, mask=False)

popt, chi2 = dataset.fit()

dataset.plot_fit()

dataset.print_total()
