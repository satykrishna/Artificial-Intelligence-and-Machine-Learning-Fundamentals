from sklearn import model_selection
from sklearn import neighbors
features_train, features_test, label_train, label_test =
model_selection.train_test_split(
 scaled_features,
 label,
 test_size=0.2
)

classifier = neighbors.KNeighborsClassifir()
classifier.fit(features_train, label_train)
classifier.score(features_test, label_test)