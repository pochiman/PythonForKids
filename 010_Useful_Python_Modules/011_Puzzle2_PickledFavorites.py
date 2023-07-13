import pickle
favorites = ['PlayStation', 'Fudge', 'Movies', 'Python for Kids']
f = open('favorites.dat', 'wb')
pickle.dump(favorites, f)
f.close()

import pickle
f = open('favorites.dat', 'rb')
favorites = pickle.load(f)
print(favorites)