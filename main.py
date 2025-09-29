'''
on importe les variables
'''
#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    '''
    on commence par la fonction itérative
    '''
    l=[]
    c=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            c+=1
        else:
            l.append((s[i-1],c))
            c=1
    l.append((s[-1],c))
    return l

def artcode_r(s):
    '''
    on fait la fonction récursive
    '''
    if not s:
        return []
    result=[]
    c=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            c+=1
        else:
            result.append((s[i-1],c))
            c=1
    result.append((s[-1],c))
    return result

#### Fonction principale


def main():
    '''
    on print les deux fonctions secondaires
    '''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
