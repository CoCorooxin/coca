#### coca
https://test.pypi.org/project/coca/ 


coca is a spell checker for French language based on levenshstein distance and Peter Norvig generative algorithm. It can detect French spelling errors within 2 edit distance.

The user can download the package via the following command line:
```cli
pip install -i https://test.pypi.org/simple/ coca==1.2.4
```
Once downloaded, the package can be used like any other python library via 'import coca'

```python
>>from coca.ortho_correct import OrthoCorrect
#create an instance of the corrector 
>>corrector = OrthoCorrect() 
#choose the automatic correction mode for your french text
>>corrector.correctionAutomatique("J'aime du cocolate.")
#this return a tuple, the first element is the corrected string the second element is a list of all the detected errors [(error1, corrected forme1), (error2, corrected forme2)...]
>>("J'aime du chocolat.", [("cocolate", "chocolat")])
#an easy way to get the results
>>corrected, analyse = corrector.correctionAutomatique("J'aime du cocolate.")
>>corrected
>>"J'aime du cocolat."
>>analyse
>>[("cocolate", "chocolat")]
#or
>>corrected = corrector.correctionAutomatique("J'aime du cocolate.")[0]
>>"J'aime du cocolat."
#choose the interactif correction mode
>>corrector.correctionInteratif("J'aime du cocolate.")
>>forme fautive détectée: cocolate
..dans le contexte : "J'aime du cocolate."
..Veuillez choisir une correction possible : .."chocolat", "not found"
.."chocolat" 
>>"J'aime du chocolat."
#correct a single word in french
>>corrector.corrigeMotAuto("cocolate")
>>"chocolat"
```

ortho_correct includes also a simple and intuitive tokenizer.

```python
>>corrector.tokenizer("Harry aime du chocolat.")
>>["Harry", "aime", "du", "chocolat", "."]
```

