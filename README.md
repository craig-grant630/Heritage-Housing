
# Overview

Lydia Doe, a Belgian resident, recently inherited four properties located in Ames, Iowa, USA. Although she is knowledgeable about real estate markets in her home country, she recognizes that property valuation principles may differ significantly in the American Midwest. To avoid inaccurate estimations and ensure profitable sales, Lydia seeks a data-driven approach to determine the market value of her new assets.

This project is developed to support Lydia in:

Accurately estimating the sales price of the four inherited homes.

Gaining insights into which house attributes most strongly affect pricing in Ames.

Building a flexible and user-friendly web application capable of predicting house prices based on input features for any property in Ames, Iowa.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

As a good friend, you are requested by your friend, who has received an inheritance from a deceased great-grandfather located in Ames, Iowa, to  help in maximising the sales price for the inherited properties.

Although your friend has an excellent understanding of property prices in her own state and residential area, she fears that basing her estimates for property worth on her current knowledge might lead to inaccurate appraisals. What makes a house desirable and valuable where she comes from might not be the same in Ames, Iowa. She found a public dataset with house prices for Ames, Iowa, and will provide you with that.

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

**Hypotheses 1**
We consider the price of houses to be higher if the house has had a larger surface measured sq. ft.

* A correlation study can help in investigating if this is true.

**Hypotheses 2**
We consider the price oh houses to be higher if the house was built more recently.

* A correlation study can help in investigating if this is true.

**Hypotheses 3**
We consider the house price to be higher if the house is in good condition.

* A correlation study can help in investigating if this is true.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

**Business Requirement 1: Correlation Analysis and Data Visualisation**
The client’s primary goal is to uncover which property features most significantly influence the house sale price.

* Dataset Review and Exploration: Begin by thoroughly examining the housing dataset to understand its structure, contents, and key attributes.

* Correlation Analysis: Use both Pearson and Spearman correlation methods to evaluate the strength and direction of the relationships between various features and the target variable, "SalePrice".

* Identify Key Influential Variables: Highlight the features that show the strongest correlation with sale price. These variables will become the focus of deeper analysis.

* Visual Analysis: Leverage visualisation tools such as scatter plots, regression lines, and heatmaps to effectively display the relationships between selected features and the sale price.

* Hypothesis Testing: Use insights gained from correlation analysis and visual tools to confirm or challenge assumptions about which property characteristics have the greatest impact on pricing.

## ML Business Case

**Key Deliverables:**

* **Data Visualisation:** Deliver clear visual representations that illustrate the relationship between various housing features and their corresponding sale prices.

* **Sale Price Estimation:** Enable accurate price predictions for the client’s inherited properties, as well as any other residential homes in Ames, Iowa.

**Analytical Approach:**

* **Traditional Data Analysis:** Apply standard statistical methods to evaluate how property attributes relate to sale prices through a detailed correlation study.

**Dashboard Development:**

* **Interactive Dashboard:** The final results will be shared through an interactive dashboard created with Streamlit, offering a user-friendly way to explore findings and predictions.

**Model Selection:**

* Given the nature of the dataset, a regression-based model will be employed to estimate house sale prices. The model will use selected housing features as input variables and produce a predicted sale price as the output.

## Dashboard Design

### Page 1: Project Overview
  
* Project Introduction
  
This project involves analyzing a dataset containing property sale information from Ames, Iowa. The goal is to understand the factors that influence house prices and develop a tool to predict the sale price of individual homes based on their attributes.

* Business Objectives

The client wishes to:

* Identify which house features are most strongly related to the final sale price.

* Use that insight to forecast the market value of four inherited properties, as well as any future houses in Ames.

### Page 2: Project Hypothesis & Validation

* Hypothesis

Certain property features — such as living area, overall quality, and basement finish — have a strong influence on house sale prices in Ames, Iowa. If these attributes are accurately captured, a predictive model should be able to estimate house prices with reasonable accuracy.

* Validation Approach

To test this, I:

* Explored correlations and predictive strength of individual features (e.g., Pearson correlation and Predictive Power Score).

* Handled missing data and engineered features where necessary.

* Trained and tested machine learning models using historical house sale data

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the .python-version Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)

* In case you would like to thank the people that provided support through this project.
