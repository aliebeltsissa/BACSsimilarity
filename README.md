<h1> BACS Similarity Experiment </h1>
This experiment was created in order to check whether the BACS characters chosen for the bilingual affix experiment have a similar similarity matrix as a single set seen in the similarity checks performed in the <a href="https://doi.org/10.3758/s13428-016-0844-8">original BACS paper by Vidal, Content, & Chetail (2017)</a>. The selected characters are a mix of upper- and lowercase BACS1, chosen by excluding any very similar upper- and lowercase characters for each distinct Latin letter.

<h2> The Repository </h2>
Contains
<ul>
	<li><strong>BACS similarity experiment notes.txt</strong>: notes on the experiment, unresolved questions, residual thoughts</li>
	<li><strong>BACS1.otf</strong>: the BACS font file</li>
	<li><strong>BACSsimilarity_PARTICIPANT_SESSION_2023-06-01_15h57.01.351.csv</strong>: an example output of the data from a practice session (note: done with a shortened version of the task)</li>
	<li><strong>example.png</strong>: a screenshot of a trial from the main task</li>
	<li><strong>index.html</strong>: the experiment script
	<li><strong>README.md</strong>: this readme file
</ul>

<h2> The Philosophy </h2>
In order to remain as loyal to the original study as possible, efforts have been made to recreate the behavioural similarity study as described in the paper. Differences remain, however: the orignal study was administered in person, and involved a familiarisation phase that is not (for the moment) present in the current study. The present study also involves more characters than the original, which makes necessary the presence of more testing blocks.

<h2> The Experiment Script </h2>
Is divided into a few sections:
<h3> Initiation </h3>
Contains the initialisation of jsPsych, the link with Pavlovia, and a few simple page setup parameters: fixing the page background to beige, setting the text colour to white. A progress bar is also set to be displayed at the top of the screen throughout the experiment.

<h3> Stimuli Generation </h3>
This section assembled the characters into pairs for the experiment. All 24 uppercase BACS1 characters plus 16 lowercase BACS1 characters were selected, for a total of 40 characters. The characters are paired together in every possible combination (40 X 40 = 1600 combinations). These are organised in a list of 2-character lists. This code takes only the first 800 combinations - see the <a href="https://github.com/aliebeltsissa/BACSsimilarity_part2">second part of the code</a> for the other half of the stimuli.

The Fisher Yates shuffle is defined as a function (`FisherYatesShuffle`) to ensure an entirely randomised shuffle, which is then applied to the list of character pairs. This means that while every participant would see every combination, they would see them in a randomised order. This order is logged to the console.

<h3> Experiment </h3>    
These are the screens using jsPsych displayed to the participants.    
<strong>Welcome screen </strong>     
A simple screen with the standard data storage information, and basic knowledge of the study.

<strong> Consent screen </strong>    
A list of consent statements to be ticked by the participants. It is required to tick all of these to proceed to the experiment. The participant's selection of these items is stored in the final data output.

<strong> Instructions screen </strong>    
Brief instructions: informing the participant that they need to determine how similar two characters are on a 0-1 scale, with 0 being very dissimilar and 1 very similar.

<strong> Example screen </strong>     
Below is the example.png file, showing an example of a trial of the main experiment task:
<img src='example.png' height='300px'>   
This is shown to participants at this time.

<strong> Dividing the stimuli into blocks </strong>    
The stimuli (character pairs) are split into 20 different blocks of 80 character pairs each. These are compiled into a `big_html` list containing, for each block separately, the HTML code needed to display the stimuli correctly at each trial. This is returned as a dictionary for each trial, containing the HTML and the two characters shown.

<strong> Blocks </strong>     
The 20 blocks of stimulus presentation are essentially identical. Block 1 begins by setting a counter for block number (`n`>). The appropriate list item from `big_html` is selected, and saved as `block_stimuli`.

The jsPsych modules follow. First, a single trial is defined as `similarity_trial`. This is set as a continuous slider going from 0 to 1, but coded as 0 to 100 out of necessity (jsPsych doesn't like working with decimals). Next, `similarity_procedure_block` sets the timeline for each trial, connecting `similarity_trial` with `block_stimuli`. This is followed by an inter-block screen, stating the number of blocks finished out of the total 20. It also suggests to participants to take a short break.

<h3> Questionnaire </h3>     
This asks demographic questions and a (very) bried language background. The original paper had 18-19 participants, and reported them only as have normal or normal-to-corrected vision, and being native French speakers.

This questionnaire asks for age and sex of participants. The language sections asks participants the nature, proficiency, and age of acquisition of up to four languages. A final question asks whether they know any further languages.

<h3> Goodbye </h3>       
Finally, a screen thanks participants for their time. The link with Pavlovia is closed.