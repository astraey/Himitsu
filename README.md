<h1>Himitsu :ocean:</h1>

<p>Encrypt text and embed it into files as audio, video or image data.</p> 

<p>For now, our platform consists of a desktop client that works with audio files. Right now, I am working on the image and video
modules, so you can embed messages in those type of files as well. For now, it is capable of reading audio files .wav, interpreting 
its frequency spectrum and modifying the values of those frequencies. The key of the idea is to cut out the frequencies from 
the audio file which are inaudible for the human ear. Then, a combination of frequencies is added in the non-audible range in 
order to encode a message in the form of text provided by the user. When the encryption is completed, a new audio file is 
created, which contains the original audio plus the encoded message. The idea is that at this point, the user sends the 
audio file to someone, that will proceed with the decoding.</p>

<p>The second step is the decoding of the encrypted file, where the user will open the audio file with our platform and will 
decode it, receiving the original message.</p>

<p>This way, because we store the data as audio, even if someone wanted to intercept the message, it would only find a 
regular audio file. Plus, because we have used non-audible frequencies, the original audio file and the file with the 
encoded message will sound exactly the same. The attacker not only would have to break the encryption, but it would also 
have know that there is a message encoded within a regular audio file.</p>

<p>To run the program, you just need to execute the following command:</p>

```
python3 gui.py
```

<p>Python 3.6.x is required, as well as the libraries tkinter and numpy</p>
