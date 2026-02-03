# PhotoHub
Legacy near-infrared galaxy photometry and star-subtraction pipeline built during my PhD for IRSF J/H/K imaging of HI-selected galaxies. The workflow supports interactive galaxy identification, PSF modeling and star subtraction, isophotal and total photometry, and publication-quality postage stamps.

This code base underpins the analysis in Said et al. 2016 (MNRAS 462, 3386). See the ADS entry here:
```
https://ui.adsabs.harvard.edu/abs/2016MNRAS.462.3386S/abstract
```

**Highlights**
- DS9-driven inspection of J/H/K fields with interactive galaxy marking.
- PSF construction with IRAF/DAOPHOT + SExtractor and iterative star subtraction.
- Ellipse and isophote fitting for surface-brightness profiles, isophotal radii, and total magnitudes.
- Automated multi-band outputs and RGB postage stamps for QC and publication.

**Repository Layout**
- `findgal.py` interactive field browser to mark galaxies and HI counterparts; writes `*.cat` and `*.hicat` lists.
- `runsubpsf.py` PSF creation, star subtraction, residual cleaning, and postage-stamp generation.
- `photometry.py` ellipse fitting, surface-brightness profiles, isophotal radii/magnitudes, and catalog output.
- `samps.py` helper to build RGB stamps and update FITS headers.

**Pipeline Overview**
1. Identify galaxies in J/H/K fields and write target lists (`findgal.py`).
2. Build PSFs, subtract stars, and clean residuals (`runsubpsf.py`).
3. Compute surface-brightness profiles and photometric measurements (`photometry.py`).
4. Generate RGB postage stamps for QC or figures (`runsubpsf.py`, `samps.py`).

**Inputs**
- Calibrated J/H/K FITS images with WCS headers.
- HI catalog and field lists (e.g., `hicatlist`, `masterHIv`, `calibrated_list`).
- Optional per-field galaxy lists (`*.hicat`) with RA/Dec and ellipse parameters.

**Outputs**
- Star-subtracted cutouts: `gal_{band}{field}_{n}_starsub.fits`.
- PSF products: `*.psf.fits`, `*.pst`, `*.psg`.
- Photometry catalogs: `nircat` and per-object `*.nircat` entries.
- Surface-brightness plots and RGB postage stamps.

**Dependencies**
This is a legacy Python 2 code base and expects classic astronomy tooling:
- Python 2.6/2.7
- IRAF + PyRAF (including `daophot` and `isophote`)
- DS9 + `pyds9`
- SExtractor (`sex` on PATH)
- NumPy, SciPy, Matplotlib
- PyFITS (now `astropy.io.fits`), PyWCS (now `astropy.wcs`)
- APLpy, astLib
- asciidata

The code also references helper modules and scripts not included here:
- `ds9disp.py`
- `skyvgrad.py`
- `iso_star_select` (external command)

**Configuration**
Paths are hard-coded near the top of each script and must be updated to your environment before running. Key variables include:
- `imagepath`, `catpath`, `psfpath`, `stamppath`, `tmppath`
- `SEconfig`, `SEparam`, `SEnnw`
- Catalog files such as `hicatlist`, `masterHIv`, and `calibrated_list`

**Quick Start (Legacy Workflow)**
This code is interactive and expects DS9 windows for QC and manual clicks.

1. Update the hard-coded paths in `findgal.py`, `runsubpsf.py`, and `photometry.py`.
2. Start DS9 and mark galaxies:
```
python2 findgal.py
```
3. Build PSFs, subtract stars, and make stamps:
```
python2 runsubpsf.py
```
4. Run photometry on star-subtracted images:
```
python2 photometry.py
```

**Known Limitations**
- System-specific absolute paths are embedded in the scripts.
- Python 2 and IRAF/PyRAF are end-of-life; a modern port would target Python 3 + Astropy.
- Several helper modules referenced in the code are not included in this repo.

**Modernization Plan (Python 3 + Astropy)**  
This is a practical path to migrate the pipeline while preserving scientific behavior.

1. **Environment + packaging**  
   - Convert to Python 3, add `pyproject.toml`, and lock dependencies.  
   - Replace `pyfits`/`pywcs` with `astropy.io.fits` and `astropy.wcs`.

2. **IRAF/PyRAF replacement strategy**  
   - Replace IRAF `ellipse` with `photutils.isophote` for isophotal fitting.  
   - Replace IRAF `daophot` steps with `photutils.psf` and `photutils.detection` where feasible.  
   - Keep legacy IRAF path as a validation baseline during migration.

3. **Star subtraction pipeline**  
   - Swap SExtractor + DAOPHOT loops for `photutils` source detection + PSF modeling.  
   - Use astropy convolution / sigma-clipping for sky estimation and cleaning.

4. **Data + config refactor**  
   - Replace hard-coded paths with a YAML config and CLI flags.  
   - Move constants (pixel scale, thresholds) into a versioned config.

5. **Reproducibility + tests**  
   - Add unit tests for key photometry functions using small FITS fixtures.  
   - Add a regression test comparing key metrics (e.g., R20, m20) to legacy outputs.

6. **Compute scale**  
   - Optional: chunked processing using Dask or Ray for batch fields.  
   - Containerize with Docker for portable, reproducible runs.

**Citation**
If you use or adapt this workflow, please cite:
```
Said et al. 2016, MNRAS, 462, 3386
```
