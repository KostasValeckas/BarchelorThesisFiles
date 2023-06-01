### These are the directories that hold the setup files needed to excecute the different main runs for GRB230325A and standard star objects. 

'AT_STAR' directory is for the setup used to reduce the standard star observartion belonging to the AT2017gfo dataset, as this star observation was used in further processing instead of the one from GRB230325A dataset, due to better fluxing results.

'GRB_STAR' directory is for the setup used to reduce the standard star observartion belonging to the GRB230325A dataset.

'SCIENCE_2dONLY' directory is for the setup used to excecute the main run on the GRB230325A target, without manual object tracing.

'SCIENCE_manualTRACE' directory is for the setup used to excecute the main run on the GRB230325A target, with manual object tracing.

```bash
├── Masters
├── QA
├── Science
├── vlt_xshooter_nir_Star/Sciene.calib
├── vlt_xshooter_nir_Star/Sciene.log
├── vlt_xshooter_nir_Star/Sciene.pypeit
└── vlt_xshooter_nir_Star/Sciene_UTC_2023-05-30.par

```

where 'Masters' holds the master frames, 'QA' holds the quality assesment plots, 'Science' holds the science products, '.calib', '.log' and '.par' are automatically produced calibration, log and parameter descriptions and the '.pypeit' file is the main run setup file.

To excecute any of the main runs, use following command:

run_pypeit SETUP_FILE_PATH . 


'setup_files' are raw output from running the setup command: 

pypeit_setup −s vlt_xshooter_nir −r . −c all −b

and are only provided for refference.

All '.fits' files in 'Master' directories have been gzipped to keep the size within 'GitHub' limits.

