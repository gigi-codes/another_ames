# Project 2: Another take on Ames, Iowa Housing Data Set 
I sought to explore the dataset with a very deliberate look at the quantitiative vs qualitative variables. I conjectured that quantitiaive (sq ft, # bed/baths) features would build a suficienty robust model, but found that the quantitiative (human-assessed) qualities were necessary to improve the model beyond the nearly 50/50 baselin. 

The following study is posed as a scientist within a real-estate agency seeking to determine an appropriate market value, both for purchase and sale, of properties in Ames, Iowa. 
---
---
---
Because of the detailed dataset available, we've selected Ames, Iowa to model and potentially invest. Furthermore, being a univeristy town, the housing demand is unlikely to collapse, and the market will be sustained by professors, staff, other univeristy workers and of course students. 


Models to predict prices initially only use numerical variables, but categorical features are iteratively incorporated. Select numeric features are one-hot encoded to be modelled as categorical, which improves model performance. 

---
## File Descrptions: 
* 01_EDA_and_Cleaning.ipynb <br>
Initial findings and data cleaning. 

* 02_Feature_Engineering_and_Modeling.ipynb <br>
Iterative inclusion of significant features to refine model using custom module; takes two arguements, `X` and `y`, prints metrics for linear regression (using cross-validation), Ridge and LASSO; plots LINE assumptions and model performance: 


> A module with function `mymets` takes a clean, dummified `X` and `y`, and returns error metrics and plots to asses LINE assumptions: 

```
import mymetrics as m
m.mymet (X,y) 
```

---
## CLEANING
Features chosen for model-inclusion were selected based on preliminary correalation metrics, and collinear ones dropped.  Select categorical features based on EDA were dummified. 

## RESULTS
### Models 1 - 3 : 
20 features numeric-only OLR. `1` and `2` used the same features, `2` was scaled but did not improve effect. `Model 3` added one feature. 


Model   | Feature Engineering           | R2        | R2, X-val     | RMSE          | Slope         | Intercept             
---     | ---                           | ---       | ---           | ---           | ---           | ---    
1       | All Numeric                   | 0.7241    | 0.7109        | 41317         | 19.94344      | -1364941
2       | Standard Scalar               | 0.7241    | 0.7109        | 41317         | 19.94344      | -1364941
3       | Included `frontage`    | 0.7398   | 0.7174    | 41875 | -24.2397  | -1123871

### Models 4-9: 
Additional Ridge and LASSO modeling. 

Model| # Feature Engineering              | R2        | R2, X-val     | RMSE          |Ridge Train    | Ridge Test      | Lasso Train  | Laso Test       
---  | ---                              | ---       | ---           | ---           | ---           | ---    | ---  | --- 
4    | `22` Garage, Fireplace as NUMERIC     | 0.7964    | 0.7841        | 35 441        | 0.8127        | 0.761         | 0.814      | 0.756621
5    | `22` Garage, Fireplace as CATEGORICAL | 0.8148     | 0.799         | 33 799       | 0.8277          | 0.7898    | 0.8278    | 0.7854
6    | `26` Utilities, categorical   | 0.8193 | 0.8016 | 33 829 | 0.8310 | 0.7945 | 0.832 | 0.7890
7 | `26` QUALITY as CATEGORICAL |  0.8405| 0.8199 | 31 364 | 0.8530 | 0.8099 | 0.8553 | 0.8071 
8 | `28` frontage + alley | 0.8409 | 0.8198 | 31 332 | 0.8533 | 0.8101 | 0.8557 | 0.8072
9 | `32` porch features | 0.8458 | - negative? | 30 843 | 0.8571 | 0.8171 | 0.8593 | 0.8152


## CONCLUSION: 

Initial analysis from a strict numerial perspective yieled good results, but the increases in model performace were laregely due to inclusion of categorical variables, as well as converting certain numericals (bedroom #, garage car capacity) to categorical. 

Qualitative metrics are significant: to ensure appropriate appraisal, Zillow should contact local assessors to inform methods for ranking, and contract for additional assessments on specific properties that the model failed to represent. 