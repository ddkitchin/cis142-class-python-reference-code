class Question :
 
   def __init__(self)->None :
      self._text = ""
      self._answer = ""
      
   def setText(self, questionText:str) ->None:
      self._text = questionText

   def setAnswer(self, correctResponse:str) ->None:
      self._answer = correctResponse

   def checkAnswer(self, response:str) ->bool:
      return response == self._answer

   def display(self)->None :
      print(self._text)         

class ChoiceQuestion(Question):
 
   def __init__(self) ->None:
      super().__init__()
      self._choices = []

   def addChoice(self, choice:str, correct:str)->None :
      self._choices.append(choice)
      if correct :
         # Convert len(choices) to string.
         choiceString = str(len(self._choices))
         self.setAnswer(choiceString)
   
   # Override Question.display().
   def display(self) ->None:
      # Display the question text.
      super().display()
      
      # Display the answer choices.
      for i in range(len(self._choices)) :
         choiceNumber = i + 1
         print(f"{choiceNumber:d}: {self._choices[i]}")
            
