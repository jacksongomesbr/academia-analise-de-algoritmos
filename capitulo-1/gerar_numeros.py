import numpy, pandas
dados = pandas.DataFrame(numpy.random.choice(range(100), 10, replace=False))
dados.to_csv('dataset-1-a.csv', header=False, index=False)