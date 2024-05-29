Optical alignment precedes the following steps. The 532 nm beam must be well aligned and vertically perpendicular after the objective lens


> Angle (vertical + horizontal) are extremely important otherwise can't see all circles in Pattern B
> Ensure Vertical + horizontal angle is zero
> Save settings file for FOIL and set the cropping factor 
> Load DMD_FOV ROI into FOIL with full CCD frame shown (skip)
> restart FOIL
> Calibrate DMD using Pattern B (matlab: TransformIdentifier.m)
> Draw ROI on FOIL full frame. Save and export ROI
> Run python compute.py in cmd
> Inject RB (40ug/g of Body Weight, 15 mg/mL concentraion of RB in Saline)
> python project.py
> Put mouse back on treadmill. Ensure that headbar angle was not changed.
> Do not change Z axis of the translation stage. You can only move X-Y 
> remove the ND filter from green path
> keep ROI ON and Full Frame FOIL ON
> XY axis align using translation stage (final adjust. No time)
> Put filter on 785 nm
> increase optical power to 0.1 AOM modulation
> restart FOIL
> Load FOIL software + settings file
> Start recording







TO DO:

> check power of DMD (good)
> check horizontal alignment (bad)
> check centering w.r.t IOS + LSCI (good)
> Fix shutter for 532nm 
> fix power supply for arduino 
> 0.07
