# Hello!
# Welcome to Threeza. You should have received an email like the below. If not, go to https://algorithmia.com/algorithms/threezaemails/Register


def welcome_message(email_alias,private_key,public_key):
    return """<html> <p>You're in !</p>
<h2>Welcome to the Intech Supercollider Challenge</h2>
<p>Brought to you by <a href="https://www.intechinvestments.com/">Intech Investments</a> using the Algorithmia Marketplace, this game
pits your mathematical talent against the complex structure of multiple stock price comovements. It requires you to deploy an algorithm that generates 10,000 samples
from the joint distribution of minutely price changes for every stock in a portfolio, every minute of the day. </p>
<h3>This sure beats bitcoin mining</h3>
<p>You can start participating, and earning, by&nbsp;<a href="https://algorithmia.com/developers/algorithm-development/your-first-algo#create-your-first-algorithm">creating your first algorithm</a>. Delete any pre-populated code and cut and paste the following:&nbsp;</p>
<pre><span style="background-color: #ffffff;">import algoz
algoz.subscribe('intech_supercollider')

def apply(input):
    output = algoz.examples.empirical_sampler( input )
    algoz.predict( output )

   </pre>
<p>Make sure to add "algoz" to the list of Algorithm dependencies (see&nbsp;<a href="https://algorithmia.com/developers/faqs/can-i-use-external-libraries">FAQ: dependencies</a>&nbsp;in the Algorithmia help). Then:&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; <span style="background-color: #99ccff; color: #ffffff;">Save</span>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="color: #ffffff;"><span style="background-color: #339966;">Build</span>&nbsp; &nbsp; &nbsp;</span></p>
<p><span style="color: #ffffff;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<span style="background-color: #333399;">Publish</span></span>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; and start earning credits. If you get to $100 or more
you will have the option to <a href='https://algorithmia.com/developers/faqs/how-do-i-make-money'>cash out</a>.
get to </p>
<h3>Give us a wave</h3>
<p>Your communications alias is EMAIL_ALIAS. Please temporarily add it to your Algorithmia username as per <a href='https://algorithmia.com/users/microprediction'>this example</a> until
we let you know you are on our radar.
<h3>Let us help</h3>
Optionally, you can add EMAIL_ALIAS to the description (doc page) for your Algorithmia algorithm which subscribes to Threeza. We will take this hint and provide you with Algorithm diagnostics.
If it gets to be too much you can simply remove it.
</p>
<h3>As a matter of formality...</h3>
<p><em>You may not need to know this</em> but your private key ending in <b>PRIVATE_KEY</b> has already been saved to your Algorithmia <a href="https://algorithmia.com/data/hosted/">data collection</a>. Never supply it to anyone. Your public key, already waved to the crowd, is <b>PUBLIC_KEY</b> </p>
<h3>Enjoy</h3>
<p>Thanks for helping with this experiment in collective probabilistic modeling of high dimensional joint distributions. See <a href="www.3za.org">www.3za.org</a> for more about this and other challenges.</p>

</html>""".replace("EMAIL_ALIAS",email_alias).replace("PRIVATE_KEY",private_key[-4:]).replace("PUBLIC_KEY",public_key)
