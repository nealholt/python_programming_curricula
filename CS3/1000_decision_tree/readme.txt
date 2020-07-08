
========= Project Steps

Step 1: split up and process data set. Function: getDogData()
Step 2: get alphabet for relevant categories. Function: getAlphabet(data, column)
Step 3: get information entropy for relevant categories. Functions: getColumn(data, column) and getEntropy(data_list, alphabet)
Step 4: Generate decision tree based on list of attributes and single target. For instance:
	Given owner age, owner gender, and city, recommend/predict a dog breed
	Given dog breed, age, gender, and color predict owner's age 
This is a big step. You need to create: class DecTreeNode, getLowestEntropyAtt(data,attribute_indicies,target), splitOnAttribute(data,column), getSplitsEntropy(splits, alphabet, target)
Another thing that can be confusing here is that we want low entropy, high information. We want to split on an attribute that divides all of our target attributes into separate buckets. We want something like gender to predict hair length. We are looking for what category, when you split on it, minimizes entropy of the target within the category.
Step 5: Debugging:
	A. Get it running at all
	B. Print what was split on and the decrease in entropy at each split.
	C. If you are getting an entropy of zero, make sure that the alphabet and the values match up. I had an issue in which I was getting the alphabet from the wrong column by accident.
STEP 6: Randomly partition data set into training and testing portions. Function: getRandomPartition(data, ratio)
STEP 7: Evaluate accuracy of decision tree.

Possible error if the training set does not contain all the same attribute values as the test set. I fixed this in a hacky way in the decision tree's predict function.


========= Understanding Decision Trees

https://medium.com/@chiragsehra42/decision-trees-explained-easily-28f23241248

https://towardsdatascience.com/light-on-math-machine-learning-intuitive-guide-to-understanding-decision-trees-adb2165ccab7


========= Bias and sexism in data and AI

Statistical types of bias (stuff like sampling bias and selection bias):

https://data36.com/statistical-bias-types-explained/

Article on the bias in datasets that results in things like gender inequality:

https://searchenterpriseai.techtarget.com/feature/Big-data-throws-big-biases-into-machine-learning-data-sets

Amazon fucked up:

https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G

https://slate.com/business/2018/10/amazon-artificial-intelligence-hiring-discrimination-women.html


========= Data sets for beginners:

https://www.kaggle.com/rtatman/fun-beginner-friendly-datasets

https://www.tableau.com/learn/articles/free-public-data-sets

Downloaded: Dogs of Zurich
https://www.kaggle.com/kmader/dogs-of-zurich

