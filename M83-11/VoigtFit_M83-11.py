import VoigtFit
import scipy.constants
import numpy as np

data_file = 'M83-11_HI_1215_lsf_mask_testerrors.reg'
lsf_file = 'M83_11_COS_LSF_TOTAL_G130M_1291_LP3.dat'

target = 'M83-11'
z_sys = 0.

ion = 'HI_1215'

dataset = VoigtFit.DataSet(z_sys)

### Name output file
dataset.set_name(target)


# -- Load Data and input to the dataset
wl, flux, err,mask = np.loadtxt(data_file, usecols=(0,1,2,4), unpack=True)

dataset.add_data(wl, flux,err=err, res=lsf_file,mask=mask, nsub=6,
                 normalized=True) 

# -- Specify the line to be analyzed
dataset.add_line(ion, velspan=20000)


#--- Add components
#                               ion     z   b     logN
dataset.add_component_velocity('HI',11., 100., 20.57, var_N=False, var_z=False, var_b=False)
dataset.add_component_velocity('HI', 508.1, 0.5, 20., var_z=False, var_b=False)

# -- And fit the dataset
dataset.prepare_dataset(norm=True, mask=True)

popt, chi2 = dataset.fit()

dataset.plot_fit()

dataset.print_total()
