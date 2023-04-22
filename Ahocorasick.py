patterns = ['aab', 'abc', 'cba']
tekst = 'aaabc'


class AhoCorasick:
    def __init__(self, patterns):
        self.patterns = patterns
        self.trie = []

    def __repr__(self):
        return repr(self.trie)

    def nastepny_stan(self, stan, litera):
        for wezel in self.trie[stan][
            'nastepny_stan']:
            if self.trie[wezel][
                'litera'] == litera:
                return wezel
        return None

    def build(self):

        self.trie.append({'litera': '', 'obecny_stan': 0, 'nastepny_stan': [], 'fail_link': 0,
                          'wzorzec': []})
        for x in patterns:
            stan = 0
            literka = 0
            nastepnik = self.nastepny_stan(stan, x[
                literka])
            while nastepnik != None:
                stan = nastepnik
                literka += 1
                if literka < len(x):
                    nastepnik = self.nastepny_stan(stan, x[literka])
                else:
                    break
            for i in range(literka,
                           len(x)):
                self.trie[stan]['nastepny_stan'].append(
                    len(self.trie))
                self.trie.append({'litera': x[i], 'obecny stan': len(self.trie), 'nastepny_stan': [], 'fail_link': 0,
                                  'wzorzec': []})
                stan = len(self.trie) - 1
            self.trie[stan]['wzorzec'].append(x)
        print(self.trie)
        self.fail_linki()
        print(self.trie)

    def fail_linki(self):
        kolejka = []
        nastepnik = 0
        for wezel in self.trie[0][
            'nastepny_stan']:
            kolejka.append(wezel)
            self.trie[wezel]['fail_link'] = 0
        while kolejka:
            remove = kolejka.pop(0)
            for nastepnik in self.trie[remove]['nastepny_stan']:
                kolejka.append(nastepnik)
                stan = self.trie[remove][
                    'fail_link']

                self.trie[nastepnik]['fail_link'] = self.nastepny_stan(stan, self.trie[nastepnik][
                    'litera'])
                if self.trie[nastepnik][
                    'fail_link'] is None:
                    self.trie[nastepnik]['fail_link'] = 0

    def search(self, tekst):
        stan = 0
        znalezione = []
        for i in range(0, len(tekst)):
            while self.nastepny_stan(stan, tekst[
                i]) is None and stan != 0:
                stan = self.trie[stan]['fail_link']
            stan = self.nastepny_stan(stan, tekst[i])
            if stan is None:
                stan = 0
            else:
                for j in self.trie[stan]['wzorzec']:
                    znalezione.append({'indeks': i - len(j) + 1, 'wzorzec': j})
        print(znalezione)


ahocorasick = AhoCorasick(['aab', 'abc', 'cba'])
ahocorasick.build()
ahocorasick.search('aaabc')
print(repr(ahocorasick))