<h1>Braille Music</h1>

![Test Image 3](/BMlogo2.png)

<h1>Purpose.</h1>
<p>
Any person writing music uses music notation software. Music software to composers is like an IDE to a programmer. Currently programs like MuseScore, which allow artist to share their sheet music to the world, are not inclusive to the visually impaired. As a result, those lacking sight are forced to purchase expensive, slow, and outdated software or pay an expert to manually trancribe their sheet music. To solve this problem we have created Braille Music, a software that automates the process of transcription from sheet music to Braille. With Braille Music people can now print out Braille sheet music at no cost.
</p>
<h1>Behind The Scenes.</h1>
<p>
It all starts with a MuseScore file. We picked this file type as a starting point because of how widely used it is within the world of music. Through our program the MuseScore file is converted to a musicxml file. After that we parse the musical data and generate a BRF file according to Brailles music notation. BRF files, endorsed by the National Library Service for the blind and deaf, are made specifically to be embossed by Braille printed.
</p>
Credit: https://github.com/markomanninen/pybrl, helped convert from ASCII to braille.

<img
src=“old.jpg”
raw=true
alt=“Subject Pronouns”
style=“margin-right: 10px;”
/>

<img
src=“new.jpg”
raw=true
alt=“Subject Pronouns”
style=“margin-right: 10px;”
/>
