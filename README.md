--------------
# <p style="text-align:center">Vancomycin AUC Calculator</p> <a name="header"></a>

![](Images/LandingPage00.png)

> Most current excel file: &#9658; <ins>**[VancomycinCalculator.xlsm](https://github.com/kpessa/vanco-auc/raw/master/VancomycinCalculator.xlsm)**</ins> &#9668;

> Most current word doc: &#9658; <ins>**[AUC_MIC Vancomycin Dosing Update20200617.docx](https://github.com/kpessa/vanco-auc/raw/master/Vancomycin%20Dosing%20Handout/AUC_MIC%20Vancomycin%20Dosing%20Update20200617.docx)**</ins> &#9668;

> Most current powerpoint ppt: &#9658; <ins>**[Vancomycin Bulletins MD RN LAB.pptx](https://github.com/kpessa/vanco-auc/raw/master/Vancomycin%20Dosing%20Handout/Vancomycin%20Bulletins%20MD%20RN%20LAB.pptx)**</ins> &#9668;

> Link to ASHP, IDSA, PIDS, and SIPD joint guidelines: &#9658; <ins>**[Vancomycin Monitoring Guidelines](https://academic.oup.com/ajhp/article/77/11/835/5810200)**</ins>&#9668;

--------------
# <p style="text-align:center">Table of Contents <a name="toc"></a></p>

* [About The AUC24/MIC Calculator](#about) 
* [Pharmacist Vancomycin AUC24/MIC Workshop](#workshop)

- [Patient Example 1: **"New Consult"**](#ex1)
	1. [Patient Information](#ptinfo)
	2. [Kidney Function](#kidney)
	3. [Loading Dose (LD)](#ld)
	4. [Volume of Distribution (Vd)](#vd)
	5. [Vancomycin Clearance (CLVanco)](#clvanco)
	6. [Maintenance Dose Table (MD)](#md)
	7. [Levels / Labs](#labs)
	8. [Progress Note](#note)
	9. [Monitoring Form](#form)

[&#8592; previous section](#header) | [&#9650; back to header](#header) | [next section &#8594;](#about)

---

#### <p style="text-align:center">About The AUC24/MIC Calculator <a name="about"></a></p>

This vancomycin calculator uses a variety of published pharmacokinetic equations and principles to estimate an initial vancomycin dosing regimen for a patient based on population estimates. Subsequently, a regimen may be calculated based two vancomycin levels for severe MRSA infections. The AUC24/MIC is calculated using the trapezoidal method.

[&#8592; previous section](#toc) | [&#9650; back to table of contents](#toc) | [next section &#8594;](#workshop)

--------------
### <p style="text-align:center">Pharmacist Vancomycin AUC<sub>24</sub>/MIC Workshop <a name="workshop"></a></p>
1. Patient example
2. Patient problems (2)
	- Empiric Dosing
	- 2 Levels with first dose
	- 2 Levels at steady state

[&#8592; previous section](#about) | [&#9650; back to table of contents](#toc) | [next section &#8594;](#ex1)

--------------
### <p style="text-align:center">Patient Example 1: **"New Consult"** Summary<a name="ex1"></a></p>
1. [Patient Information](#ptinfo)
	- [**Steps**](#ptinfosteps)
	- [** Further Reading: **](#furtherreading) 
		1. ***`MRN`*** used / needed to save patient information to database
		2. No info on first page technically required to proceed
		3. ***Anthropomorphics***: `TBW/IBW` and `BMI`
		4. ***Conversions***: for `Height` and `Weight`
2. [Kidney Function](#kidney)
3. [Loading Dose (LD)](#ld)
4. [Volume of Distribution (Vd)](#vd)
5. [Vancomycin Clearance (CLVanco)](#clvanco)
6. [Maintenance Dose Table (MD)](#md) 
7. [Levels / Labs](#labs)
8. [Progress Note](#note)
9. [Monitoring Form](#form)

[&#8592; previous section](#workshop) | [&#9650; back to table of contents](#toc) | [next section &#8594;](#ptinfo)

--------------
### 1. Patient Information <a name=ptinfo></a>
* 41 yo female with MRSA Osteomyelitis
* Wt: 88.9 kg
* Ht: 157 cm 

----

##### Steps <a name=ptinfosteps></a>

<details><summary>1. Choose the New Consult button</summary>

![](Images/selectnewconsult.png)</details>

<details><summary>2. Enter the patient information into the calculator</summary>

![](Images/ptinfoinput.png)</details>

<details><summary>3. Select "Next" button. Choosing Next will save the information automatically.</summary>

![](Images/ptinfonext.png)</details>

#### Further Reading <a name="furtherreading"></a>

<details><summary>1. MRN used / needed to save patient information to database <a name=ptinfocomments></a></summary>
 
#### **`MRN`** used / needed to save patient information to database

![](Images/ptinfo11.png)</details>

<details><summary>2. Previously added patients can be identified and loaded in the “Load Patient Information” section</summary>

![](Images/ptinfoload.png)</details>

<details><summary>3. No info on first page technically required to proceed </summary>

![](Images/ptinfo2.png)</details>

<details><summary>4. Anthropomorphics: TBW/IBW and BMI </summary>

#### ***Anthropomorphics***: `TBW/IBW` and `BMI`
* If `Age`, `Height`, `Weight` and `Gender` are inputted, `TBW/IBW` and `BMI` are calculated and displayed in patient information ribbon.

![](Images/ptinfo_bmi.png)

</details>

<details><summary>5. Conversions: for Height and Weight</summary>

#### Conversions: for `Height` and `Weight`

- For **`Height`**, can either input as ***`cm`s*** or ***`ft/in`s***

![](Images/ptinfo3.png)

- For **`Weight`**, can either input as ***`kgs`*** or ***`lbs`***

![](Images/ptinfo4.png)</details>

[&#8592; previous section](#ex1) | [&#9650; back to example summary](#ex1) | [next section &#8594;](#kidney)

-------

### 2. Kidney Function <a name=kidney></a>
* SCr: 0.5 (stable)
* no concurrent nephrotoxic drugs
* no amputations

-------

##### Steps <a name=kidneysteps></a>

<details><summary>1. Manually-enter CrCl or enter SCr</summary>

#### 1. Manually-enter CrCl or enter `SCr`
* If entering `SCr`, then press `Next` button

![](Images/kidney000.png)</details>
	
<details><summary>2. If patient is muscle wasted or cachectic, the SCr can be rounded by selecting “Yes”</summary>

#### 2. If patient is muscle wasted or cachectic, the `SCr` can be rounded by selecting “Yes”

![](Images/kidneySCr.png)</details>

<details><summary>3. If patient is obese (>120% IBW) the AdjBW can be used to calculate CrCl by selecting “Yes”</summary>

#### 3. If patient is obese (>120% IBW) the `AdjBW` can be used to calculate CrCl by selecting “Yes”

![](Images/kidneyTBW_IBW.png)</details>

<details><summary>4. Select “Accept ### ml/min as CrCl”</summary>

#### 4. Select “Accept ### ml/min as CrCl” 

![](Images/kidneyAccept.png)</details>

[&#8592; previous section](#ptinfo) | [&#9650; back to example summary](#ex1) | [next section &#8594;](#ld)

### 3. Loading Dose (LD) <a name=ld></a>

> New IDSA Vancomycin Guidelines from March 2020 recommend giving a loading dose for critically ill patients, ICU patients, those that require dialysis or renal replacement therapy.  

<details><summary>"Click here" to see image of guidelines</summary>

![](Images/LoadingDoses.jpg)</details>

##### Steps

<details><summary>1. Consider whether patient requires a loading dose and if so, what category they fall into, and select “Calculate Load” or “No Load”.</summary>  

#### 1. Consider whether patient requires a loading dose and if so, what category they fall into, and select “Calculate Load” or “No Load”.  

![](Images/ld_click0.png)</details>

•	Loading dose max  will be hospital specific, but according new guidelines may go up to 3000 mg.
•	Calculator will estimate what time the loading dose will be given, adjust time based on expectations (consider time to dispense and potential delay from administering other antibiotics before vancomycin) 


**[&#9650; <ins>back to table of contents</ins>](#toc)**
### 4. Volume of Distribution (Vd) <a name=vd></a>
**[&#9650; <ins>back to table of contents</ins>](#toc)**
### 5. Vancomycin Clearance (CLVanco) <a name=clvanco></a>
**[&#9650; <ins>back to table of contents</ins>](#toc)**
### 6. Maintenance Dose Table (MD) <a name=md></a> 
**[&#9650; <ins>back to table of contents</ins>](#toc)**
### 7. Levels / Labs <a name=labs></a>
**[&#9650; <ins>back to table of contents</ins>](#toc)**
### 8. Progress Note <a name=note></a>
**[&#9650; <ins>back to table of contents</ins>](#toc)**
### 9. Monitoring Form <a name=form></a>
**[&#9650; <ins>back to table of contents</ins>](#toc)**