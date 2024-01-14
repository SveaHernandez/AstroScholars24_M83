import VoigtFit
import scipy.constants
import numpy as np

data_file = 'M83-12_HI_1215_vel_mask.reg'
lsf_file = 'M83_12_COS_LSF_TOTAL_G130M_1291_LP3.dat'

target = 'M83-12'
z_sys = 0.

ion = 'HI_1215'

dataset = VoigtFit.DataSet(z_sys)

### Name output file
dataset.set_name(target)


# -- Load Data and input to the dataset
wl, flux, err,mask = np.loadtxt(data_file, usecols=(0,1,2,4), unpack=True)

dataset.add_data(wl, flux,err=err, res=lsf_file, mask=mask,nsub=6,
                 normalized=True)

# -- Specify the line to be analyzed
dataset.add_line(ion, velspan=15000)


#--- Add components
#                               ion     z   b     logN
dataset.add_component_velocity('HI',16., 100., 20.57, var_N=False, var_z=False, var_b=False)
dataset.add_component_velocity('HI', 524.9, 0.5, 20.15, var_z=False, var_b=False)


# -- And fit the dataset
dataset.prepare_dataset(norm=True, mask=True)

popt, chi2 = dataset.fit()

dataset.plot_fit()

dataset.print_total()
