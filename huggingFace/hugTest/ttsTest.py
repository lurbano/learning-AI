# from transformers import pipeline
# import soundfile as sf

# synthesizer = pipeline("text-to-speech", "suno/bark-small")

# speech = synthesizer("Look I am generating speech in three lines of code!")

# sf.write("voiceTest.wav", speech["audio"], speech["sampling_rate"])




# from transformers import pipeline
# import scipy

# synthesiser = pipeline("text-to-speech", "suno/bark-small")

# speech = synthesiser("Hello, my dog is cooler than you!", forward_params={"do_sample": True})

# scipy.io.wavfile.write("bark_out.wav", rate=speech["sampling_rate"], data=speech["audio"])


from bark import SAMPLE_RATE, generate_audio, preload_models
import soundfile as sf

preload_models()

text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)

sf.write("voiceTest.wav", audio_array, SAMPLE_RATE)
