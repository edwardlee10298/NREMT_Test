"""
App.py for EMT_TEST

# Edward Lee (eal265)
# Last Updated: 1/18/2025
"""
from consts import *
from game2d import *
from game2d import GLabel


class App(GameApp):
    """
    This is only class for this applications

    Since the testing application uses a three part system, all of them
    are defined under the same class
    """

    # THREE MAIN GAMEAPP METHODS
    def start(self):
        """
        Initializes the application.

        This is the title screen of EMT_TEST
        There are other attributes that are defined below
        """
        # IMPLEMENT ME
        self._state = "STATE_INACTIVE"
        self._question = None
        self._clickchecker = False
        self._main = GLabel(text="",font_name = 'ComicSans.ttf',font_size=13, \
            x=GAME_WIDTH/2, y=230)
        self._option1 = GLabel(text="",font_name = 'ComicSans.ttf',\
            font_size=16, x=GAME_WIDTH/2, y=200)
        self._option2 = GLabel(text="",font_name = 'ComicSans.ttf',\
            font_size=16, x=GAME_WIDTH/2, y=170)
        self._option3 = GLabel(text="",font_name = 'ComicSans.ttf',\
            font_size=16, x=GAME_WIDTH/2, y=140)

        self._explanation1 = GLabel(text="",font_name = 'ComicSans.ttf',\
            font_size=16, x=GAME_WIDTH/2, y=GAME_HEIGHT-40)
        self._explanation2 = GLabel(text="",font_name = 'ComicSans.ttf',\
            font_size=16, x=GAME_WIDTH/2, y=GAME_HEIGHT-60)
        self._point = 0
        self._correct = False
        self._dingSound = Sound("ding3.wav")
        self._question1audio = Sound("question1.wav")
        self._question2audio = Sound("question2.wav")
        self._question3audio = Sound("question3.wav")

        if self._state == "STATE_INACTIVE":
            self._text = GLabel(text="Press SPACE to Begin Exam",font_name = \
                'ComicSans.ttf',font_size=50, x=GAME_WIDTH/2, y=GAME_HEIGHT/2)
        else:
            self._text = None

    def update(self,dt):
        """
        This updates the game progress
        """
        #THE BEGINING SCREEN
        if self._state == "STATE_INACTIVE":
            if self._input.is_key_released("spacebar"):
                self._state = "STATE_INTRO"

        #THE SLIDES THAT GIVES THE INSTRUCTIONS
        if self._state == "STATE_INTRO":
            self._explanation1 = GLabel(text="This exam is meant to measure the user's",font_name = 'ComicSans.ttf',font_size=20, \
                x=GAME_WIDTH/2, y=GAME_HEIGHT-240)
            self._explanation2 = GLabel(text="abilities to take the NREMT exam",\
                font_name = 'ComicSans.ttf',font_size=20, x=GAME_WIDTH/2, y=GAME_HEIGHT-260)
            self._explanation3 = GLabel(text="At the end, you will recieve a score from pass to fail" ,\
                font_name = 'ComicSans.ttf',font_size=20, x=GAME_WIDTH/2, y=GAME_HEIGHT-280)
            self._explanation4 = GLabel(text="Press SPACE to Continue" ,\
                font_name = 'ComicSans.ttf',font_size=40, x=GAME_WIDTH/2, y=GAME_HEIGHT-340)

            if self.input.is_key_down("spacebar"):
                self._clickchecker = True
            if self.input.is_key_released("spacebar") and self._clickchecker:
                self._clickchecker = False
                self._question1audio.play()
                self._state = "STATE_A1"

        #QUESTION A1 INTROUDCTION
        if self._state == "STATE_A1":

            self._explanation1 = GLabel(text="Questions for A1 Level: Please listen to the audio and follow along below",\
                font_name = 'ComicSans.ttf',font_size=16, x=GAME_WIDTH/2, y=GAME_HEIGHT-35)
            self._explanation2 = GLabel(text="Press SPACE when you are ready",\
                font_name = 'ComicSans.ttf',font_size=16, x=GAME_WIDTH/2, y=GAME_HEIGHT-65)
            self._question = GImage(x=GAME_WIDTH/2,y=GAME_HEIGHT-270,width=600\
                ,height=320,source="question1.png")

            if self.input.is_key_down("spacebar"):
                self._clickchecker = True
            if self.input.is_key_released("spacebar") and self._clickchecker:
                self._clickchecker = False
                self._state = "STATE_A1a"

        if self._state == "STATE_A1a":
            self._question1audio.volume = 0

            self._explanation1.text = "QUESTION 1"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 1] What is the first intervention the EMT does "
            self._option1.text = "a.) check for a pulse"
            self._option2.text = "b.) check for scene safety"
            self._option3.text = "c.) address any life-threatning bleeding"
            self.answer_b_isright("STATE_A1b")

        if self._state == "STATE_A1b":
            self._explanation1.text = "QUESTION 2"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 2] Which of these questions is not asked for an AMS patient?"
            self._option1.text = "a.) last known normal"
            self._option2.text = "b.) glucose levels"
            self._option3.text = "c.) number of current sexual partners"
            self.answer_c_isright("STATE_A1c")

        if self._state == "STATE_A1c":
            self._explanation1.text = "QUESTION 3"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 3] Is the current respiratory rate high, low, or normal?"
            self._option1.text = "a.) high"
            self._option2.text = "b.) low"
            self._option3.text = "c.) normal"
            self.answer_a_isright("STATE_A1d")

        if self._state == "STATE_A1d":
            self._explanation1.text = "QUESTION 4"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 4] When glucose levels are confirmed on the extreme, what are next steps?"
            self._option1.text = "a.) give oral glucose"
            self._option2.text = "b.) administer insulin"
            self._option3.text = "c.) do nothing"
            self.answer_a_isright("STATE_A1e")

        if self._state == "STATE_A1e":
            self._explanation1.text = "QUESTION 5"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 5] The patient likely took a fall as well, what are next steps"
            self._option1.text = "a.) look for knee fractures"
            self._option2.text = "b.) check for bleeding"
            self._option3.text = "c.) spine stabalization / c-collar"
            self.answer_c_isright("finala1")

        if self._state == "finala1":
            if self._point >= 3:
                self._point = 0
                self._question2audio.play()
                self._state = "STATE_A2"
            else:
                self._result = "A1"
                self._state = "OVER"


        #QUESTION A2 INTROUDCTION
        if self._state == "STATE_A2":
            self._explanation1 = GLabel(text="Questions for A2 Level: Please listen to the audio and follow along below",\
                font_name = 'ComicSans.ttf',font_size=20, x=GAME_WIDTH/2, y=GAME_HEIGHT-35)
            self._explanation2 = GLabel(text="Press SPACE when you are ready",\
                font_name = 'ComicSans.ttf',font_size=20, x=GAME_WIDTH/2, y=GAME_HEIGHT-65)
            self._question = GImage(x=GAME_WIDTH/2,y=GAME_HEIGHT-270,width=600,\
                height=320,source="question2.png")
            self._main.text = ""
            self._option1.text = ""
            self._option2.text = ""
            self._option3.text = ""

            if self.input.is_key_down("spacebar"):
                self._clickchecker = True
            if self.input.is_key_released("spacebar") and self._clickchecker:
                self._clickchecker = False
                self._state = "STATE_A2a"

        if self._state == "STATE_A2a":
            self._question2audio.volume = 0
            self._explanation1.text = "QUESTION 1"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 1] Which revealed fact about the patient would cause you to initiate an extensive special report?"
            self._option1.text = "a.) the patient refuses to take their meds"
            self._option2.text = "b.) high irritability"
            self._option3.text = "c.) suspected elder abuse"
            self.answer_c_isright("STATE_A2b")

        if self._state == "STATE_A2b":
            self._explanation1.text = "QUESTION 2"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 2] When examining the patient, the patient has a sucking chest wound. What would you do as an intervention?"
            self._option1.text = "a.) direct pressure"
            self._option2.text = "b.) chest seal"
            self._option3.text = "c.) chest glue"
            self.answer_b_isright("STATE_A2c")

        if self._state == "STATE_A2c":
            self._explanation1.text = "QUESTION 3"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 3] When talking to geriatric patients, what is the manner that you should speak to them in?"
            self._option1.text = "a.) use a louder voice"
            self._option2.text = "b.) use the same voice as other patients"
            self._option3.text = "c.) use a slower voice"
            self.answer_b_isright("STATE_A2d")

        if self._state == "STATE_A2d":
            self._explanation1.text = "QUESTION 4"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 4] Is the current blood glucose level of the patient high, low, or normal?"
            self._option1.text = "a.) high"
            self._option2.text = "b.) low"
            self._option3.text = "c.) normal"
            self.answer_c_isright("STATE_A2e")

        if self._state == "STATE_A2e":
            self._explanation1.text = "QUESTION 5"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 5] What is bruising under the eyes commonly called?"
            self._option1.text = "a.) battle signs"
            self._option2.text = "b.) clickers"
            self._option3.text = "c.) raccoon eyes"
            self.answer_c_isright("finala2")

        if self._state == "finala2":
            if self._point >= 3:
                self._point = 0
                self._question3audio.play()
                self._state = "STATE_B1"
            else:
                self._result = "A1"
                self._state = "OVER"


        #QUESTION B1 INTROUDCTION
        if self._state == "STATE_B1":
            self._explanation1 = GLabel(text="Questions for B1 Level: Please listen to the audio and follow along below",\
                font_name = 'ComicSans.ttf',font_size=20, x=GAME_WIDTH/2, y=GAME_HEIGHT-35)
            self._explanation2 = GLabel(text="Press SPACE when you are ready",\
                font_name = 'ComicSans.ttf',font_size=20, x=GAME_WIDTH/2, y=GAME_HEIGHT-65)
            self._question = GImage(x=GAME_WIDTH/2,y=GAME_HEIGHT-270,width=600,\
                height=320,source="question3.png")
            self._main.text = ""
            self._option1.text = ""
            self._option2.text = ""
            self._option3.text = ""

            if self.input.is_key_down("spacebar"):
                self._clickchecker = True
            if self.input.is_key_released("spacebar") and self._clickchecker:
                self._clickchecker = False
                self._state = "STATE_B1a"

        if self._state == "STATE_B1a":
            self._explanation1.text = "QUESTION 1"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 1] What should be your first intervention after scene safety and you are next to the patient?"
            self._option1.text = "a.) start compressions"
            self._option2.text = "b.) check for a pulse"
            self._option3.text = "c.) find and attach an AED"
            self.answer_b_isright("STATE_B1b")

        if self._state == "STATE_B1b":
            self._explanation1.text = "QUESTION 2"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 2] What is the rate of compressions for CPR?"
            self._option1.text = "a.) 100-120 bpm"
            self._option2.text = "b.) 200-210 bpm"
            self._option3.text = "c.) 60-80 bpm"
            self.answer_a_isright("STATE_B1c")

        if self._state == "STATE_B1c":
            self._explanation1.text = "QUESTION 3"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 3] What are the rates of compressions and ventalations for when there are 2 EMT's?"
            self._option1.text = "a.) 15-1"
            self._option2.text = "b.) 45-2"
            self._option3.text = "c.) 30-2"
            self.answer_c_isright("STATE_B1d")

        if self._state == "STATE_B1d":
            self._explanation1.text = "QUESTION 4"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 4] When should you check for a pulse?"
            self._option1.text = "a.) after every AED shock"
            self._option2.text = "b.) once at the beginning"
            self._option3.text = "c.) never check for a pulse"
            self.answer_b_isright("STATE_B1e")

        if self._state == "STATE_B1e":
            self._explanation1.text = "QUESTION 5"
            self._explanation2.text = "On your keyboard, press a,b,or c"
            self._main.text = "[Question 5] Which cycle is ROCC most likely?"
            self._option1.text = "a.) electrical"
            self._option2.text = "b.) metabloic"
            self._option3.text = "c.) circulatory"
            self.answer_a_isright("finalb1")

        if self._state == "finalb1":
            if self._point >= 3:
                self._point = 0
                self._state = "WIN"
            else:
                self._result = "A1"
                self._state = "OVER"

        if self._state == "OVER":
            self._explanation4 = GLabel(text="To try to test again, press SPACE",\
                font_name = 'ComicSans.ttf',font_size=40, x=GAME_WIDTH/2, y=GAME_HEIGHT-340)
            self._explanation3 = GLabel(text="You did not pass the exam",\
                font_name = 'ComicSans.ttf',font_size=40, x=GAME_WIDTH/2, y=GAME_HEIGHT-300)

            if self.input.is_key_down("spacebar"):
                self._clickchecker = True
            if self.input.is_key_released("spacebar") and self._clickchecker:
                self._clickchecker = False
                self._point = 0
                self._main.text = ""
                self._option1.text = ""
                self._option2.text = ""
                self._option3.text = ""
                self._state = "STATE_INTRO"

        if self._state == "WIN":
            self._explanation4 = GLabel(text="To try to test again, press SPACE",\
                font_name = 'ComicSans.ttf',font_size=40, x=GAME_WIDTH/2, y=GAME_HEIGHT-340)
            self._explanation3 = GLabel(text="You passed the exam!",\
                font_name = 'ComicSans.ttf',font_size=40, x=GAME_WIDTH/2, y=GAME_HEIGHT-300)

            if self.input.is_key_down("spacebar"):
                self._clickchecker = True
            if self.input.is_key_released("spacebar") and self._clickchecker:
                self._clickchecker = False
                self._point = 0
                self._main.text = ""
                self._option1.text = ""
                self._option2.text = ""
                self._option3.text = ""
                self._state = "STATE_INTRO"


    def answer_a_isright(self,next_stage):
        if self.input.is_key_down("a"):
            self._clickchecker = True
            self._correct = True
        if self.input.is_key_down("c") or self.input.is_key_down("b"):
            self._clickchecker = True
        if (self.input.is_key_released("a") or self.input.is_key_released("b") \
            or self.input.is_key_released("c")) and self._clickchecker:
            if self._correct == True:
                self._point = self._point + 1
            self._clickchecker = False
            self._correct = False
            self._dingSound.play()
            self._state = next_stage

    def answer_b_isright(self,next_stage):
        if self.input.is_key_down("b"):
            self._clickchecker = True
            self._correct = True
        if self.input.is_key_down("a") or self.input.is_key_down("c"):
            self._clickchecker = True
        if (self.input.is_key_released("a") or self.input.is_key_released("b") \
            or self.input.is_key_released("c")) and self._clickchecker:
            if self._correct == True:
                self._point = self._point + 1
            self._clickchecker = False
            self._correct = False
            self._dingSound.play()
            self._state = next_stage

    def answer_c_isright(self,next_stage):
        if self.input.is_key_down("c"):
            self._clickchecker = True
            self._correct = True
        if self.input.is_key_down("a") or self.input.is_key_down("b"):
            self._clickchecker = True
        if (self.input.is_key_released("a") or self.input.is_key_released("b") \
            or self.input.is_key_released("c")) and self._clickchecker:
            if self._correct == True:
                self._point = self._point + 1
            self._clickchecker = False
            self._correct = False
            self._dingSound.play()
            self._state = next_stage


    def draw(self):
        """
        Draws the game objects to the view.
        """
        # IMPLEMENT ME
        if self._state == "STATE_INACTIVE":
            self._text.draw(self.view)

        elif self._state == "STATE_INTRO":
            self._explanation1.draw(self.view)
            self._explanation2.draw(self.view)
            self._explanation3.draw(self.view)
            self._explanation4.draw(self.view)

        elif self._state == "OVER":
            self._explanation3.draw(self.view)
            self._explanation4.draw(self.view)

        elif self._state == "WIN":
            self._explanation3.draw(self.view)
            self._explanation4.draw(self.view)

        else:
            self._explanation1.draw(self.view)
            self._explanation2.draw(self.view)
            self._question.draw(self.view)
            self._main.draw(self.view)
            self._option1.draw(self.view)
            self._option2.draw(self.view)
            self._option3.draw(self.view)
