
import pickle

def pickle_stats(wins=0, losses=0):
    stats = {
        'wins': wins,
        'losses': losses,
    }
    try:
        old_stats = pickle.load(open('assets/stats.dat', 'rb'))
    except:
        old_stats = {
            'wins': 0,
            'losses': 0,
        }
    new_stats = dict(old_stats)
    new_stats.update(stats)
    for i, n in old_stats.items():
        for x, y in stats.items():
            if i == x:
                new_stats[i] = (n + y)
    pickle.dump(new_stats, open('assets/stats.dat', 'wb'))


def get_stats():
    try:
        return pickle.load(open('assets/stats.dat', 'rb'))
    except:
        return {'wins': 0, 'losses': 0}
