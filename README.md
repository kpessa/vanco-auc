# Vancomycin AUC Calculator

![](Images/LandingPage0.png)

# Table of Contents
1. [About The AUC24/MIC Calculator](#about) 
2. [Pharmacist Vancomycin AUC24/MIC Workshop](#workshop)
3. [Patient Example 1: **"New Consult"**](#ex1)

#### About The AUC24/MIC Calculator <a name="about"></a>

This vancomycin calculator uses a variety of published pharmacokinetic equations and principles to estimate an initial vancomycin dosing regimen for a patient based on population estimates. Subsequently, a regimen may be calculated based two vancomycin levels for severe MRSA infections. The AUC24/MIC is calculated using the trapezoidal method.

# Pharmacist Vancomycin AUC24/MIC Workshop <a name="workshop"></a>
1. Patient example
2. Patient problems (2)
	- Empiric Dosing
	- 2 Levels with first dose
	- 2 Levels at steady state

## Patient Example 1: **"New Consult"** <a name="ex1"></a>
1. [Patient Information](#ptinfo)
	- [**Steps**](#ptinfosteps)
	- [** Comments: **](#ptinfocomments) 
		1. ***`MRN`*** used / needed to save patient information to database
		2. No info on first page technically required to proceed
		3. ***Anthropomorphics***: `TBW/IBW` and `BMI`
		4. ***Conversions***: for `Height` and `Weight`
2. [Kidney Function](#kidney)

### 1. Patient Information <a name=ptinfo></a>
* 41 yo female with MRSA Osteomyelitis
* Wt: 88.9 kg
* Ht: 157 cm

##### Steps <a name=ptinfosteps></a>

1. Choose the New Consult button
2. Enter the patient information into the calculator and choose Next. Choosing Next will save the information automatically.
3. Select save to add/update information in database 
4. Entering the medical record number will allow patient to be identified during future admissions in the database
5. Previously added patients can be identified and loaded in the “Load Patient Information” section

![](Images/ptinfo0.png)

##### **Comments:** <a name=ptinfocomments></a>
 
![](Images/ptinfo11.png)
![](Images/ptinfo2.png)

#### ***Anthropomorphics***: `TBW/IBW` and `BMI`
* If `Age`, `Height`, `Weight` and `Gender` are inputted, `TBW/IBW` and `BMI` are calculated and displayed in patient information ribbon.

![](Images/ptinfo_bmi.png)

#### Conversions: for `Height` and `Weight`

- For **`Height`**, can either input as ***`cm`s*** or ***`ft/in`s***

![](Images/ptinfo3.png)

- For **`Weight`**, can either input as ***`kgs`*** or ***`lbs`***

![](Images/ptinfo4.png)

### 2. Kidney Function <a name=kidney></a>
* SCr: 0.5 (stable)
* no concurrent nephrotoxic drugs
* no amputations

##### Steps <a name=kidneysteps></a>
1. Manually-enter CrCl or enter `SCr`
	* If entering `SCr`, then press `Next` button


	