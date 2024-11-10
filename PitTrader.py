import random
import time
from gtts import gTTS
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

def generate_and_play_number(rounds,roundNo,EV):
    
    probability = random.randint(0,100)
    

    bid = random.randint(0,1)
    single = random.randint(0,1)

    if single:   
        if bid:
            if probability<=70 and probability >= 5:
                tts = gTTS("bid "+str(random.randint(EV-3,EV)))
            elif probability < 5:
                tts = gTTS("bid "+str(random.randint(EV+2,EV+6)))
            else:
                tts = gTTS("bid "+str(random.randint(EV,EV+2)))
        else:
            if probability>70 and probability <= 95:
                tts = gTTS(" offered at "+str(random.randint(EV-2,EV)))
            elif probability > 95:
                tts = gTTS(" offered at "+str(random.randint(EV-6,EV-2)))
            else:
                tts = gTTS(" offered at "+str(random.randint(EV,EV+3)))

    else:
        if probability<=80:
            tts = gTTS(str(random.randint(EV-4,EV))+" at "+str(random.randint(EV,EV+4)))
        else:
            tts = gTTS(str(random.randint(EV,EV+2))+" at "+str(random.randint(EV-2,EV)))
        
    # Save the audio to a file
    audio_file = "number_audio.mp3"
    tts.save(audio_file)
    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio_file)
    sound.play()
    while pygame.mixer.get_busy():
        continue
    pygame.mixer.quit()

def main():
    print("Press Ctrl+C to stop the program.")
    EV = 25
    rounds = 10
    print("The next EV is...")
    for i in range(rounds):
        EV += random.randint(-4,4)
        print(EV)
        tts = gTTS(str(EV)+" is the next number")
        audio_file = "number_audio.mp3"
        tts.save(audio_file)
        pygame.mixer.init()
        sound = pygame.mixer.Sound(audio_file)
        sound.play()
        while pygame.mixer.get_busy():
            continue

        pygame.mixer.quit()
        for j in range(random.randint(10,15)):           
            generate_and_play_number(rounds,i,EV)
            #time.sleep(1)  # Wait for 3 seconds before generating the next number
    print("GGWP!")
    tts = gTTS("GGWP")
    audio_file = "number_audio.mp3"
    tts.save(audio_file)
    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio_file)
    sound.play()
    while pygame.mixer.get_busy():
        continue
if __name__ == "__main__":
    main()
