---
title: Computers are alien to me
date: 2019-01-31
---

<!--kg-card-begin: html--><p>I&#8217;ve been reading a series of technical and computing books recently, as I pick up my <a href="https://en.wikipedia.org/wiki/Python_%28programming_language%29" target="_blank" rel="noopener noreferrer">Python</a> studies. I naively stumbled into coding assuming all I needed were the terms and grammar of a knew &#8220;language&#8221;. But there&#8217;s so much more to learn for someone who has mostly had a liberal arts education.</p>
<p>It&#8217;s a completely different mode of thinking. You often see coding/development described as &#8220;problem solving&#8221;, but I don&#8217;t think that is quite acurate. I have been bumbling my way through a kind of alien logic.</p>
<p>Actually, the best example comes from a recent problem I encountered on <a href="https://brilliant.org/" target="_blank" rel="noopener noreferrer">Brilliant</a>:</p>
<p>&nbsp;</p>
<blockquote><p>Define a comparison as an operation which takes in one number and tells you whether it is larger than, smaller than, or equal to, another. Suppose you are given a sorted array with 1000 elements, and you can use at most n comparisons to determine whether a certain number is in this array.&nbsp;<strong>What is the smallest value</strong> of n such that you will always be capable of making this determination, regardless of the values of the elements in the array?</p>
</blockquote>
<p>Essentially what they are asking me to do is conjure up a number and find that same number in a&nbsp;<em>sorted</em> list of 1000 numbers. What&#8217;s the smallest number of comparisons I would need to make to find the match? I sat stumped for quite a while with this problem.</p>
<p>Eventually I gave up. I couldn&#8217;t fathom how to even approach it. &nbsp;Having now seen <a href="https://en.wikipedia.org/wiki/Binary_search_algorithm" target="_blank" rel="noopener noreferrer">the solution</a> I can&#8217;t imagine I would ever have arrived there through deduction alone. It wasn&#8217;t so much a lack of knowledge of terms etc., my regular heuristics simply don&#8217;t apply.</p>
<p>Another example comes from a book called <a href="https://www.worldcat.org/title/how-software-works-the-magic-behind-encryption-cgi-search-engines-and-other-everyday-technologies/oclc/899229274&#038;referer=brief_results" target="_blank" rel="noopener noreferrer">How Software Works</a>, which I am currently working my way through. This is from a chapter on protecting passwords:</p>
<p>&nbsp;</p>
<blockquote><p>Authentication systems need a way to strengthen hashing without a performance-crushing number of hash iterations; that is, they need a method of storing passwords that requires an impractical time investment from attackers without creating an equally unrealistic time burden on legitimate access. That method is called salt&#8230; <strong>The salt is a string of characters, like a short, random password, that is combined with the user’s password before hashing.</strong> For example, user mrgutman chooses falcon as his password, and the system generates h38T2 as the salt&#8230;.</p>
<p>The salt and password can be combined in various ways, but the simplest is <strong>appending the salt to the end of the password</strong>, resulting in falconh38T2 in this example. <strong>This combination is then hashed</strong>, and the hash code stored in the authentication table along with the username and the salt&#8230;</p>
<p>If there are, say, 100,000 users in a stolen authentication table, and the salts are numerous enough that no salt is duplicated in the table, the attacker will need to create 100,000 tables. At this point, we can’t even call them precomputed tables <strong>because the attacker is creating them for each attack.</strong></p>
</blockquote>
<p>&nbsp;</p>
<p>Buried in a section about scrambling (<a href="https://en.wikipedia.org/wiki/Cryptographic_hash_function" target="_blank" rel="noopener noreferrer">not the right word I know</a>) passwords so that they cannot be reverse engineererd and easily matched, we have this interesting solution. Simply append a random string to the password before scrambling. Put this way it&#8217;s quite simple and I can follow the logic. But getting this far requires a kind of thinking to which I am unaccustomed.</p>
<p>On the surface, that different fields have different approaches isn&#8217;t particularly profound. But it&#8217;s not often that we get to feel out of our depth on a &#8220;I don&#8217;t even understand how to logic this out&#8221; level. I am definitely feeling that right now.</p>
<p>&nbsp;</p>
<p><em>(As always, my emphasis)</em></p>
<!--kg-card-end: html-->