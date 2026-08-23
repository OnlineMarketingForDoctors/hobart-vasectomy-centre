# -*- coding: utf-8 -*-
"""Body content for the interior pages. Edit here, then run build_pages.py."""

def build(write, phero, cta, crumb, TICK, BOOK):

    # ====================================================== ABOUT US ======
    about = phero(
        '/assets/generated/20-geoff-conference.webp',
        'Dr Geoff Cashion presenting at a vasectomy conference',
        'About us',
        'Two specialists. <em>One</em> procedure.',
        'Dr Geoff Cashion and Dr Matt Valentine have performed more than 32,000 '
        'vasectomies between them. It is not a sideline to a general practice &mdash; '
        'it is the whole practice.'
    ) + '''
<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker" data-rev>Why it matters</p>
        <h2 class="h2" data-rev data-rev-d="1">Volume is the quiet variable in surgery.</h2>
      </div>
      <div class="prose" data-rev data-rev-d="2">
        <p>Most men having a vasectomy are seen by a doctor who performs a handful each year. Both of ours perform them every clinic, every week. That repetition is not a marketing line &mdash; it is the mechanism behind short procedure times, low complication rates and the calm that patients notice on the table.</p>
        <p>Both trained in the no-scalpel technique in the United States. Both work exclusively in vasectomy through Vasectomy Australia, the country's largest provider of the procedure.</p>
        <div class="statrow">
          <div><b data-count="32000" data-suffix="+">32,000+</b><span>Combined procedures</span></div>
          <div><b data-count="4000" data-suffix="+">4,000+</b><span>A year, Dr Cashion</span></div>
          <div><b data-count="250" data-suffix="+">250+</b><span>A month, Dr Valentine</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--navy);color:var(--paper)">
  <div class="wrap">
    <div class="split" style="margin-bottom:clamp(40px,5vw,72px)">
      <div class="split__media" data-rev>
        <img src="/assets/generated/01-geoff-portrait.webp" width="1200" height="1607" alt="Dr Geoff Cashion in the procedure room" loading="lazy" decoding="async" style="aspect-ratio:3/4">
      </div>
      <div>
        <p class="kicker kicker--dk" data-rev>Founder</p>
        <h2 class="h2" data-rev data-rev-d="1">Dr Geoff<br>Cashion</h2>
        <div class="prose prose--dk" data-rev data-rev-d="2" style="margin-top:24px">
          <p>Geoff was born in Brisbane and grew up in Rockhampton. He graduated in medicine from the University of Queensland in 2002 and spent years in emergency medicine and general practice before narrowing his focus to a single procedure.</p>
          <p>He completed his no-scalpel vasectomy training in Florida under <strong>Dr Doug Stein</strong> &mdash; one of the most experienced vasectomists in the world &mdash; with further training in Australia. He founded Vasectomy Australia, and now performs more no-scalpel vasectomies each year than any other doctor in the country.</p>
          <p>He is a Fellow of the Australian College of Rural and Remote Medicine and of the Royal College of Emergency Medicine, and teaches general practice registrars as a GP Supervisor with James Cook University. Outside medicine he is a recording artist with two albums and a national tour behind him.</p>
        </div>
        <div class="statrow statrow--dk" data-rev data-rev-d="3">
          <div><b>15,000+</b><span>Performed to date</span></div>
          <div><b>FACRRM</b><span>Rural &amp; remote medicine</span></div>
          <div><b>FRCEM</b><span>Emergency medicine</span></div>
        </div>
      </div>
    </div>

    <div class="split split--wide" style="padding-top:clamp(34px,4vw,56px);border-top:1px solid var(--rule-dk)">
      <div>
        <p class="kicker kicker--dk" data-rev>Qualifications</p>
        <h3 class="h2" style="font-size:clamp(24px,2.4vw,34px)" data-rev data-rev-d="1">A record, in order.</h3>
      </div>
      <ol class="tl tl--dk" data-rev data-rev-d="2">
        <li><span class="tl__y">1992</span><div class="tl__c"><b>Bachelor of Business</b><span>Queensland University of Technology</span></div></li>
        <li><span class="tl__y">2002</span><div class="tl__c"><b>Bachelor of Medicine, Bachelor of Surgery</b><span>University of Queensland</span></div></li>
        <li><span class="tl__y">2011</span><div class="tl__c"><b>Fellowship, Australian College of Rural and Remote Medicine</b><span>FACRRM</span></div></li>
        <li><span class="tl__y">2013</span><div class="tl__c"><b>Fellowship, The Royal College of Emergency Medicine</b><span>FRCEM</span></div></li>
        <li><span class="tl__y">2018</span><div class="tl__c"><b>Graduate Certificate in Occupational Medicine</b><span>Otago University</span></div></li>
      </ol>
    </div>

    <div class="split split--wide" style="margin-top:clamp(40px,5vw,68px);padding-top:clamp(34px,4vw,56px);border-top:1px solid var(--rule-dk)">
      <div>
        <p class="kicker kicker--dk" data-rev>Published research</p>
      </div>
      <div class="prose prose--dk" data-rev data-rev-d="1">
        <p><strong>What is the TCI dose required when using propofol for conscious sedation during dental procedures? A retrospective study.</strong><br>
        G Cashion, G Treston. <em>The Internet Journal of Anesthesiology</em>, 2014, Vol 34 No 1.</p>
        <p style="margin-top:1.2em"><strong>What is the nature of the emergence phenomenon when using intravenous or intramuscular ketamine for paediatric procedural sedation?</strong><br>
        Treston G, Bell A, Carwell R, Fincher G, Chand D, Cashion G. <em>Emergency Medicine Australasia</em>, 2009, 21, 315&ndash;322.</p>
      </div>
    </div>
  </div>
</section>

<section class="cutband">
  <img src="/assets/generated/21-geoff-teaching.webp" width="1600" height="1195" alt="Dr Cashion demonstrating the no-scalpel technique to two other doctors" loading="lazy" decoding="async">
  <p class="cutband__cap">Teaching the no-scalpel technique</p>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--flip">
      <div class="split__media" data-rev>
        <img src="/assets/generated/02-matt-portrait.webp" width="1200" height="1607" alt="Dr Matt Valentine in a consulting room" loading="lazy" decoding="async" style="aspect-ratio:3/4">
      </div>
      <div>
        <p class="kicker" data-rev>Vasectomy specialist</p>
        <h2 class="h2" data-rev data-rev-d="1">Dr Matt<br>Valentine</h2>
        <div class="prose" data-rev data-rev-d="2" style="margin-top:24px">
          <p>In 2016 Matt travelled to the United States to train in the no-scalpel technique, adding it to an established general practice skill set. He set out to offer a procedure that was both secure and efficient, with as little downtime for the patient as possible.</p>
          <p>He is now one of Australia's foremost vasectomists, having performed more than 17,000 procedures &mdash; currently over 250 every month. He is known among referring GPs for turning urgent cases around quickly, usually within a fortnight, and makes himself available to referring doctors for advice at any time.</p>
        </div>
        <div class="statrow" data-rev data-rev-d="3">
          <div><b>17,000+</b><span>Performed to date</span></div>
          <div><b>250+</b><span>Every month</span></div>
          <div><b>2016</b><span>US-trained since</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="figband">
  <div class="figband__media"><img src="/assets/generated/05-both-prep.webp" width="1800" height="1005" alt="Dr Cashion and Dr Valentine reviewing a chart together" loading="lazy" decoding="async"></div>
  <div class="figband__scrim"></div>
  <div class="wrap figband__in">
    <h2 data-rev>Vasectomy is not something they fit in between other work.</h2>
    <p data-rev data-rev-d="1">It is the only thing they do. Every clinic, every week, for years &mdash; which is precisely why the fifteen minutes you spend on the table are unremarkable ones for them.</p>
    <ul class="check check--dk" style="margin-top:clamp(30px,4vw,48px);max-width:640px" data-rev data-rev-d="2">
      <li>''' + TICK + '''<div><b>Consultation and procedure on the same day</b><span>One trip, not two.</span></div></li>
      <li>''' + TICK + '''<div><b>Free phone consultation before you commit</b><span>Speak to the doctor, not a call centre.</span></div></li>
      <li>''' + TICK + '''<div><b>24-hour after-care support</b><span>You get direct contact details before you leave.</span></div></li>
      <li>''' + TICK + '''<div><b>No GP referral needed</b><span>Book yourself, whenever suits.</span></div></li>
    </ul>
  </div>
</section>
''' + cta('Talk to one of them first.',
          'Phone consultations are free, and you speak to the doctor who would do the procedure.')

    write('about-us.html',
          'About Us | Hobart Vasectomy Centre',
          "Dr Geoff Cashion and Dr Matt Valentine have performed more than 32,000 vasectomies between them.",
          about)

    # ============================================ PATIENT INFORMATION ====
    diagram = '''<figure class="diagram__fig" data-rev>
      <svg viewBox="0 0 920 250" role="img" aria-labelledby="dgTitle dgDesc">
        <title id="dgTitle">How the vas deferens is divided in a no-scalpel, open-ended vasectomy</title>
        <desc id="dgDesc">Three stages. First the vas deferens runs intact from the testicle towards the prostate. Second, the tube is divided: the prostatic end is sealed and the testicular end is deliberately left open. Third, a thin layer of tissue is placed between the two ends so they cannot rejoin.</desc>

        <!-- stage 1 -->
        <g transform="translate(0,0)">
          <text class="dg-key" x="0" y="16">01</text>
          <text class="dg-label" x="26" y="16">Intact</text>
          <ellipse class="dg-organ" cx="42" cy="176" rx="30" ry="38"/>
          <path class="dg-tube" d="M42 138 C42 96 96 92 150 92 L246 92"/>
          <text class="dg-label" x="0" y="238">Testicle</text>
          <text class="dg-label" x="196" y="72" text-anchor="end">Towards prostate</text>
        </g>
        <line class="dg-rule" x1="286" y1="30" x2="286" y2="220"/>

        <!-- stage 2 -->
        <g transform="translate(320,0)">
          <text class="dg-key" x="0" y="16">02</text>
          <text class="dg-label" x="26" y="16">Divided, and left open</text>
          <ellipse class="dg-organ" cx="42" cy="176" rx="30" ry="38"/>
          <path class="dg-tube" d="M42 138 C42 96 96 92 132 92"/>
          <path class="dg-tube dg-tube--cut" d="M176 92 L246 92"/>
          <path d="M170 82 L170 102" stroke="#FDED89" stroke-width="4" stroke-linecap="round"/>
          <text class="dg-label" x="112" y="132">Open end</text>
          <text class="dg-label" x="246" y="72" text-anchor="end">Sealed end</text>
        </g>
        <line class="dg-rule" x1="606" y1="30" x2="606" y2="220"/>

        <!-- stage 3 -->
        <g transform="translate(640,0)">
          <text class="dg-key" x="0" y="16">03</text>
          <text class="dg-label" x="26" y="16">Tissue barrier</text>
          <ellipse class="dg-organ" cx="42" cy="176" rx="30" ry="38"/>
          <path class="dg-tube" d="M42 138 C42 96 96 92 132 92"/>
          <path class="dg-tube dg-tube--cut" d="M182 92 L252 92"/>
          <rect class="dg-tissue" x="150" y="64" width="9" height="56" rx="4"/>
          <text class="dg-label" x="118" y="146">Fascial interposition</text>
        </g>
      </svg>
      <figcaption>Open-ended technique. Leaving the testicular end open lets sperm continue to be released and reabsorbed, which reduces pressure and congestion in the testis &mdash; and with it the risk of post-vasectomy pain. The layer of tissue placed between the two ends is what stops them finding each other again.</figcaption>
    </figure>'''

    pi = phero(
        '/assets/generated/31-procedure-wide.webp',
        'The procedure room at the Hobart Vasectomy Centre',
        'Patient information',
        'Everything that happens, <em>before</em> you agree to it.',
        'Deciding on a vasectomy can feel daunting. It usually stops feeling that way '
        'once you know exactly what the day involves. Here is the whole thing.',
    ) + '''
<section class="section">
  <div class="wrap">
    <p class="kicker" data-rev>The day itself</p>
    <h2 class="h2" data-rev data-rev-d="1">Three stages, one visit.</h2>
    <p class="lede" data-rev data-rev-d="2" style="margin-top:22px">Consultation, procedure and discharge all happen in the same appointment. Most men are here for well under an hour.</p>

    <div class="slider" data-slider style="margin-top:clamp(38px,5vw,64px)">
      <div class="slider__rail" data-rail tabindex="0" aria-label="The three stages of your visit">
        <article class="slide">
          <img src="/assets/generated/03-geoff-consult.webp" width="1600" height="1195" alt="A consultation before the procedure" loading="lazy" decoding="async">
          <p class="slide__k">Stage 01 &middot; Consultation</p>
          <h3>You talk it through, before anything else</h3>
          <p>Your doctor confirms your decision, goes through your medical history, checks nothing you are taking needs the procedure postponed, walks you through the consent form, and does a brief examination to confirm he can feel the vas on both sides.</p>
        </article>
        <article class="slide">
          <img src="/assets/generated/06-procedure-room.webp" width="1600" height="1073" alt="The procedure room" loading="lazy" decoding="async">
          <p class="slide__k">Stage 02 &middot; Procedure</p>
          <h3>Fifteen minutes in the procedure room</h3>
          <p>You meet the nurse assisting. You undress from the waist down and lie on the bed with a sheet over you. The area is cleaned with betadine to reduce infection risk, then numbed. Most men barely notice the first injection.</p>
        </article>
        <article class="slide">
          <img src="/assets/generated/23-recovery-home.webp" width="1600" height="1600" alt="Resting at home after the procedure" loading="lazy" decoding="async">
          <p class="slide__k">Stage 03 &middot; Home</p>
          <h3>You drive yourself home</h3>
          <p>The wound is closed with steri-strips &mdash; no stitches. You leave with post-operative instructions, your doctor's direct contact details, and a pathology form for the semen analysis in three months.</p>
        </article>
      </div>
      <div class="slider__nav">
        <button class="slider__btn" data-prev type="button" aria-label="Previous stage"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg></button>
        <button class="slider__btn" data-next type="button" aria-label="Next stage"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg></button>
      </div>
    </div>
  </div>
</section>

<section class="section diagram">
  <div class="wrap">
    <div class="split split--wide" style="margin-bottom:clamp(34px,4vw,52px)">
      <div>
        <p class="kicker kicker--dk" data-rev>The technique</p>
        <h2 class="h2" data-rev data-rev-d="1">What is actually done to the vas.</h2>
      </div>
      <div class="prose prose--dk" data-rev data-rev-d="2">
        <p>No scalpel is used. A single small opening is made in the front of the scrotum by blunt dissection, and both sides are reached through it. The vas is lifted out, divided, and the ends are treated differently on purpose.</p>
      </div>
    </div>
    ''' + diagram + '''
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker" data-rev>Step by step</p>
        <h2 class="h2" data-rev data-rev-d="1">In the room.</h2>
        <p class="lede" data-rev data-rev-d="2" style="margin-top:20px">The sequence below is the same every time. Your doctor will narrate it as he goes if you would rather know where you are up to.</p>
      </div>
      <ol class="tl" data-rev data-rev-d="1">
        <li><span class="tl__y">Prep</span><div class="tl__c"><b>Cleaned with betadine</b><span>An antiseptic preparation, used to reduce the chance of infection.</span></div></li>
        <li><span class="tl__y">00:00</span><div class="tl__c"><b>The skin is numbed</b><span>A small needle of local anaesthetic into the skin of the scrotum. Most men barely notice it.</span></div></li>
        <li><span class="tl__y">00:02</span><div class="tl__c"><b>A single opening is made</b><span>In the front of the scrotum. Further local anaesthetic is placed around each vas &mdash; this can feel uncomfortable for a couple of seconds.</span></div></li>
        <li><span class="tl__y">00:05</span><div class="tl__c"><b>The left vas is divided</b><span>Lifted out, its outer tissue separated, then cut and the prostatic end sealed. A tissue layer is placed between the two ends &mdash; fascial interposition.</span></div></li>
        <li><span class="tl__y">00:08</span><div class="tl__c"><b>The testicular end is left open</b><span>Cut with scissors and returned to the scrotum, deliberately open to prevent congestion and pressure.</span></div></li>
        <li><span class="tl__y">00:12</span><div class="tl__c"><b>The right vas, through the same opening</b><span>The identical sequence is repeated on the other side.</span></div></li>
        <li><span class="tl__y">00:15</span><div class="tl__c"><b>Closed with steri-strips</b><span>No stitches to come out. You are free to go.</span></div></li>
      </ol>
    </div>
  </div>
</section>

<section class="figband">
  <div class="figband__media"><img src="/assets/generated/30-recovery-kit.webp" width="1600" height="1073" alt="A simple recovery kit laid out" loading="lazy" decoding="async"></div>
  <div class="figband__scrim"></div>
  <div class="wrap figband__in">
    <p class="kicker kicker--dk" data-rev>Before the day</p>
    <h2 data-rev data-rev-d="1">Four things to sort out beforehand.</h2>
    <ul class="check check--dk" style="margin-top:clamp(28px,3.5vw,44px);max-width:680px" data-rev data-rev-d="2">
      <li>''' + TICK + '''<div><b>Stop blood thinners seven days out</b><span>Aspirin, warfarin and similar. Discuss it with your GP or specialist first &mdash; and call us on 1800&nbsp;764&nbsp;763 if you are unsure.</span></div></li>
      <li>''' + TICK + '''<div><b>Shave the scrotum on the morning</b><span>With a razor. It takes a minute and makes the preparation cleaner.</span></div></li>
      <li>''' + TICK + '''<div><b>Arrange light duties for a week</b><span>If your job involves heavy lifting or straining, book the time off or arrange light duties for seven days.</span></div></li>
      <li>''' + TICK + '''<div><b>Sign the consent form</b><span>It arrives by SMS three days before your appointment. Read it properly &mdash; it sets out every risk.</span></div></li>
    </ul>
  </div>
</section>

<section class="section" style="background:var(--paper-2)">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker" data-rev>Recovery</p>
        <h2 class="h2" data-rev data-rev-d="1">What the fortnight after looks like.</h2>
        <p class="lede" data-rev data-rev-d="2" style="margin-top:20px">Most men are back to normal in about seven days. Some are quicker; some take a fortnight. Both are ordinary.</p>
        <div class="callout callout--paper" data-rev data-rev-d="3" style="margin-top:30px;max-width:44ch">
          <p>You are not sterile the day you walk out. <b style="color:var(--navy)">Consider yourself fertile</b> until a semen analysis confirms otherwise &mdash; about three months later.</p>
        </div>
      </div>
      <ol class="tl" data-rev data-rev-d="1">
        <li><span class="tl__y">Day 0</span><div class="tl__c"><b>Drive yourself home</b><span>Ice on and off through the evening. It is the single most useful thing you can do.</span></div></li>
        <li><span class="tl__y">Days 1&ndash;2</span><div class="tl__c"><b>Take it easy</b><span>Expect some bruising and mild swelling. Simple pain relief is usually enough.</span></div></li>
        <li><span class="tl__y">Day 3</span><div class="tl__c"><b>Back to a desk job</b><span>If your work is not physical, most men are back at it. No heavy lifting.</span></div></li>
        <li><span class="tl__y">Day 7</span><div class="tl__c"><b>Back to normal, roughly</b><span>Average time to feeling yourself again. Sexual activity generally resumes about now &mdash; but you are still fertile.</span></div></li>
        <li><span class="tl__y">Week 12</span><div class="tl__c"><b>Semen analysis</b><span>The test that actually confirms it worked, once residual sperm has cleared.</span></div></li>
      </ol>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__media" data-rev>
        <img src="/assets/generated/24-pathology.webp" width="1600" height="1073" alt="A pathology sample jar and request form" loading="lazy" decoding="async" style="aspect-ratio:3/2">
      </div>
      <div>
        <p class="kicker" data-rev>The test that ends it</p>
        <h2 class="h2" data-rev data-rev-d="1">A vasectomy is not finished until the analysis says so.</h2>
        <div class="prose" data-rev data-rev-d="2" style="margin-top:24px">
          <p>The procedure does not sterilise you immediately. Sperm already past the point of division has to clear, which takes time and ejaculations, not just weeks.</p>
          <p>You go for a semen analysis roughly <strong>three months afterwards</strong>, using the pathology form we give you on the day. Until we tell you the result is clear, you and your partner should keep using contraception.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''
    write('patient-information.html',
          'Patient Information | No-Scalpel Vasectomy Explained',
          'What happens before, during and after a no-scalpel vasectomy at the Hobart Vasectomy Centre.',
          pi + '__FAQ__' + cta('Still deciding?',
                               'Book a free phone consultation and ask the doctor directly. No referral, no obligation.'))

    # ================================================== VASECTOMY FEES ====
    fees = phero(
        '/assets/generated/25-rebate-desk.webp',
        'Claiming a Medicare rebate from home',
        'Vasectomy fees',
        '$597 out of pocket. <em>No</em> asterisk.',
        "One fee, set against the Australian Medical Association's recommended schedule. "
        'No hospital admission, no anaesthetist, and nothing that arrives in the post six weeks later.'
    ) + '''
<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker" data-rev>The arithmetic</p>
        <h2 class="h2" data-rev data-rev-d="1">What you pay, and when.</h2>
        <dl class="ledger" data-rev data-rev-d="2">
          <div class="ledger__row"><dt>Vasectomy fee</dt><dd>$830</dd></div>
          <div class="ledger__row"><dt>Less Medicare rebate</dt><dd>&minus;&thinsp;$233</dd></div>
          <div class="ledger__row ledger__row--total"><dt>Out of pocket</dt><dd>$597</dd></div>
        </dl>
      </div>
      <div>
        <ol class="tl" data-rev data-rev-d="1">
          <li><span class="tl__y">On booking</span><div class="tl__c"><b>$100 deposit</b><span>Secures your appointment. See the cancellation policy for how it is treated if you need to move or cancel.</span></div></li>
          <li><span class="tl__y">On the day</span><div class="tl__c"><b>$730 balance</b><span>Paid at the clinic on the day of your procedure.</span></div></li>
          <li><span class="tl__y">Same week</span><div class="tl__c"><b>$233 back from Medicare</b><span>We submit the claim for you afterwards. The rebate lands in your bank account within one to two days.</span></div></li>
        </ol>
        <div class="callout" data-rev data-rev-d="2" style="margin-top:30px">
          <p>Net cost to you: <b>$597</b>. That is the number to plan around, and it does not move.</p>
          <p style="margin-top:.8em"><a href="/cancellation-policy" style="color:var(--blue)">Read our cancellation policy</a></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--paper-2)">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker" data-rev>The comparison worth making</p>
        <h2 class="h2" data-rev data-rev-d="1">Private health insurance usually costs you more here.</h2>
        <div class="prose" data-rev data-rev-d="2" style="margin-top:24px">
          <p>You cannot use private health insurance with us, because we work in medical centres rather than private hospitals. That sounds like bad news until you add up the hospital route.</p>
          <p>Insurance only helps when a urologist performs the procedure in a hospital or day surgery &mdash; and that path carries an excess, a surgeon's gap, and an anaesthetist's gap, because nearly all surgeons will want you asleep.</p>
        </div>
      </div>
      <div>
        <ul class="compare" data-compare data-rev data-rev-d="1">
          <li class="is-us" style="--v:26%">
            <div class="compare__top"><span class="compare__name">Here, all in</span><span class="compare__v">$597</span></div>
            <span class="compare__track"><i></i></span>
          </li>
          <li style="--v:44%">
            <div class="compare__top"><span class="compare__name">Private health excess</span><span class="compare__v">$500&ndash;$1,000</span></div>
            <span class="compare__track"><i></i></span>
          </li>
          <li style="--v:44%">
            <div class="compare__top"><span class="compare__name">Urologist gap fee</span><span class="compare__v">up to $1,000</span></div>
            <span class="compare__track"><i></i></span>
          </li>
          <li style="--v:34%">
            <div class="compare__top"><span class="compare__name">Anaesthetist fee and gap</span><span class="compare__v">additional</span></div>
            <span class="compare__track"><i></i></span>
          </li>
          <li style="--v:100%">
            <div class="compare__top"><span class="compare__name">Hospital route, insured</span><span class="compare__v">$2,000+</span></div>
            <span class="compare__track"><i></i></span>
          </li>
        </ul>
        <p class="compare__note">Hospital-route figures are indicative ranges, not quotes &mdash; excesses and gap fees vary by fund, surgeon and anaesthetist. The point is not the exact number. It is that you will not know it in advance, and with us you already do.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--navy);color:var(--paper)">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker kicker--dk" data-rev>If you have to claim it yourself</p>
        <h2 class="h2" data-rev data-rev-d="1">Four ways to get your rebate back.</h2>
      </div>
      <div class="prose prose--dk" data-rev data-rev-d="2">
        <p>We normally submit the claim for you. If you have paid in full and no claim has been lodged on your behalf, any of these four will do it.</p>
        <p>You will need your paid invoice, which we email within 48 hours of your appointment.</p>
      </div>
    </div>

    <div class="slider slider--dk" data-slider style="margin-top:clamp(38px,5vw,58px)">
      <div class="slider__rail" data-rail tabindex="0" aria-label="Four ways to claim your Medicare rebate">
        <article class="slide">
          <p class="slide__k">Option 01</p>
          <h3>Upload it online</h3>
          <p>Add a copy of your paid invoice to your Medicare Online account through myGov. The fastest route if you already have an account set up.</p>
          <a class="slide__link" href="https://www.servicesaustralia.gov.au/individuals/services/medicare/medicare-online-accounts" rel="noopener" target="_blank">Medicare online accounts <span aria-hidden="true">&rarr;</span></a>
        </article>
        <article class="slide">
          <p class="slide__k">Option 02</p>
          <h3>Use the app</h3>
          <p>Download the Express Plus Medicare mobile app and process the claim from your phone. Photograph the invoice and submit it in a couple of minutes.</p>
          <a class="slide__link" href="https://www.servicesaustralia.gov.au/individuals/services/medicare/express-plus-medicare-mobile-app" rel="noopener" target="_blank">Express Plus Medicare app <span aria-hidden="true">&rarr;</span></a>
        </article>
        <article class="slide">
          <p class="slide__k">Option 03</p>
          <h3>By mail</h3>
          <p>Complete a Medicare claim form, attach the invoice and post it. Slower, but it works without an online account.</p>
          <a class="slide__link" href="https://www.servicesaustralia.gov.au/individuals/forms/ms014" rel="noopener" target="_blank">Claim form MS014 <span aria-hidden="true">&rarr;</span></a>
        </article>
        <article class="slide">
          <p class="slide__k">Option 04</p>
          <h3>In person</h3>
          <p>Take the invoice into a Services Australia service centre and claim over the counter.</p>
          <a class="slide__link" href="https://findus.servicesaustralia.gov.au/" rel="noopener" target="_blank">Find a service centre <span aria-hidden="true">&rarr;</span></a>
        </article>
      </div>
      <div class="slider__nav">
        <button class="slider__btn" data-prev type="button" aria-label="Previous option"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg></button>
        <button class="slider__btn" data-next type="button" aria-label="Next option"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg></button>
      </div>
    </div>

    <div class="callout" data-rev style="margin-top:clamp(34px,4vw,52px);background:var(--navy-2);max-width:70ch">
      <p>Haven't had your invoice? Email <a href="mailto:info@vasectomyaustralia.com.au" style="color:var(--blue)">info@vasectomyaustralia.com.au</a> and we will resend it.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="kicker" data-rev>Included</p>
        <h2 class="h2" data-rev data-rev-d="1">What the $597 actually buys.</h2>
        <ul class="check" data-rev data-rev-d="2" style="margin-top:30px">
          <li>''' + TICK + '''<div><b>Consultation and procedure, same day</b><span>One appointment, not two.</span></div></li>
          <li>''' + TICK + '''<div><b>24-hour after-care support</b><span>Direct contact details, not a switchboard.</span></div></li>
          <li>''' + TICK + '''<div><b>Pathology form for your semen analysis</b><span>Given to you on the day.</span></div></li>
          <li>''' + TICK + '''<div><b>Medical certificate if your work needs one</b><span>On request.</span></div></li>
          <li>''' + TICK + '''<div><b>Free phone consultation before you book</b><span>With the doctor who would perform it.</span></div></li>
        </ul>
      </div>
      <div class="split__media" data-rev data-rev-d="1">
        <img src="/assets/generated/27-reception.webp" width="1600" height="893" alt="Reception at the clinic" loading="lazy" decoding="async" style="aspect-ratio:16/10">
      </div>
    </div>
  </div>
</section>
''' + cta('One fee. Booked in a couple of minutes.',
          'A $100 deposit holds your appointment. The rest is settled on the day.')

    write('vasectomy-fees.html',
          'Vasectomy Fees | $597 Out of Pocket | Hobart Vasectomy Centre',
          'No-scalpel vasectomy in Hobart for $597 out of pocket after the Medicare rebate.',
          fees)

    # ========================================================= LOCATION ====
    loc = phero(
        '/assets/generated/26-clinic-exterior.webp',
        'The medical centre exterior on a quiet suburban street',
        'Location',
        'Rosny Park, on the <em>eastern</em> shore.',
        'We run our Hobart clinics from the Clarence GP Super Clinic in Rosny Park &mdash; '
        'about ten minutes over the bridge from the Hobart CBD.'
    ) + '''
<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker" data-rev>The address</p>
        <p class="addr" data-rev data-rev-d="1" style="color:var(--ink);font-size:clamp(20px,1.8vw,28px);margin-top:0">
          <b style="display:block;font-family:var(--display);font-weight:800;font-stretch:86%;letter-spacing:-.02em">Clarence GP Super Clinic</b>
          16&ndash;22 Bayfield St<br>Rosny Park TAS 7018
        </p>
        <div style="display:grid;gap:14px;margin-top:32px" data-rev data-rev-d="2">
          <a class="btn btn--ink" href="https://maps.google.com/?q=Clarence+GP+Super+Clinic+16-22+Bayfield+St+Rosny+Park+TAS+7018" rel="noopener" target="_blank" style="justify-self:start">Open in Google Maps</a>
        </div>
        <div class="callout" data-rev data-rev-d="3" style="margin-top:32px;max-width:46ch">
          <p><b>Finding the entrance.</b> Patients tell us it can be easy to miss the first time. You can enter through the medical centre itself, or through the pharmacy next door &mdash; it has access to the centre too.</p>
        </div>
      </div>
      <div>
        <ul class="check" data-rev data-rev-d="1">
          <li>''' + TICK + '''<div><b>Ten minutes from the Hobart CBD</b><span>Straight over the Tasman Bridge and onto the eastern shore.</span></div></li>
          <li>''' + TICK + '''<div><b>Drive yourself, both ways</b><span>The procedure is under local anaesthetic, so you do not need anyone to collect you.</span></div></li>
          <li>''' + TICK + '''<div><b>Shopping-centre precinct</b><span>Rosny Park is well served for parking, food and anything you need before or after.</span></div></li>
          <li>''' + TICK + '''<div><b>Consultation and procedure in one visit</b><span>You only make the trip once.</span></div></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="cutband">
  <img src="/assets/generated/09-waiting.webp" width="1600" height="893" alt="The waiting area at the clinic" loading="lazy" decoding="async">
  <p class="cutband__cap">Waiting area &middot; Clarence GP Super Clinic</p>
</section>

<section class="figband">
  <div class="figband__media"><img src="/assets/generated/28-hobart-golden.webp" width="2400" height="1018" alt="Hobart waterfront at golden hour with Mount Wellington behind" loading="lazy" decoding="async"></div>
  <div class="figband__scrim"></div>
  <div class="wrap figband__in">
    <p class="kicker kicker--dk" data-rev>Getting here</p>
    <h2 data-rev data-rev-d="1">Worth the drive from anywhere in the south.</h2>
    <p data-rev data-rev-d="2">Men travel to us from across southern Tasmania, and it is still a single morning. Consultation, procedure and discharge happen in the one appointment, and you drive yourself home afterwards.</p>
    <div class="phero__act" data-rev data-rev-d="3">
      <a class="btn btn--gold" href="''' + BOOK + '''" rel="noopener"><span class="btn__dot"></span>Check the calendar</a>
      <a class="btn btn--ghost" href="/contact-us">Contact the centre</a>
    </div>
  </div>
</section>
''' + cta('See when we are next in Hobart.',
          'Clinics run regularly at Rosny Park. The online calendar shows the real availability.')

    write('location.html',
          'Location | Rosny Park, Hobart | Hobart Vasectomy Centre',
          'The Hobart Vasectomy Centre runs from the Clarence GP Super Clinic, 16-22 Bayfield St, Rosny Park TAS 7018.',
          loc)

    # ======================================================= CONTACT US ====
    contact = phero(
        '/assets/generated/27-reception.webp',
        'Reception at the clinic',
        'Contact us',
        'Ask us anything, <em>before</em> you book.',
        'Phone consultations with the doctor are free. There is no referral needed and '
        'no obligation to go ahead.',
        acts=False
    ) + '''
<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker" data-rev>Direct lines</p>
        <h2 class="h2" data-rev data-rev-d="1">Reach the centre.</h2>
        <ul class="check" data-rev data-rev-d="2" style="margin-top:30px">
          <li>''' + TICK + '''<div><b><a href="tel:1800764763" style="color:var(--ink);text-decoration:none">1800 SNIPME &middot; 1800 764 763</a></b><span>The quickest way to get a question answered or a free phone consultation booked.</span></div></li>
          <li>''' + TICK + '''<div><b><a href="mailto:info@vasectomyaustralia.com.au" style="color:var(--ink);text-decoration:none">info@vasectomyaustralia.com.au</a></b><span>For invoices, Medicare paperwork and anything you would rather put in writing.</span></div></li>
          <li>''' + TICK + '''<div><b>Clarence GP Super Clinic</b><span>16&ndash;22 Bayfield St, Rosny Park TAS 7018. Entry through the centre or the pharmacy next door.</span></div></li>
          <li>''' + TICK + '''<div><b><a href="https://www.facebook.com/vasectomyaustralia" rel="noopener" target="_blank" style="color:var(--ink);text-decoration:none">facebook.com/vasectomyaustralia</a></b><span>Updates from the wider Vasectomy Australia practice.</span></div></li>
        </ul>
        <div class="split__media" data-rev data-rev-d="3" style="margin-top:clamp(32px,4vw,48px)">
          <img src="/assets/generated/22-matt-phone.webp" width="1600" height="1195" alt="Dr Matt Valentine taking a phone consultation" loading="lazy" decoding="async" style="aspect-ratio:4/3">
        </div>
      </div>

      <div style="background:var(--navy);padding:clamp(26px,3.4vw,44px);color:var(--paper)" data-rev data-rev-d="1">
        <p class="kicker kicker--dk">Send a message</p>
        <h2 class="h2" style="font-size:clamp(24px,2.4vw,36px);color:var(--paper)">We answer every one.</h2>
        <form class="form" style="margin-top:28px" action="#" method="post" novalidate>
          <div class="form__row form__row--2">
            <p class="field"><label for="cf-name">Your name</label><input id="cf-name" name="name" type="text" autocomplete="name" required placeholder="First and last"></p>
            <p class="field"><label for="cf-phone">Phone</label><input id="cf-phone" name="phone" type="tel" autocomplete="tel" placeholder="Best number to reach you"></p>
          </div>
          <p class="field"><label for="cf-email">Email</label><input id="cf-email" name="email" type="email" autocomplete="email" required placeholder="you@example.com"></p>
          <p class="field"><label for="cf-topic">What is this about?</label>
            <select id="cf-topic" name="topic">
              <option>Booking a vasectomy</option>
              <option>Free phone consultation</option>
              <option>Fees and Medicare</option>
              <option>After my procedure</option>
              <option>Something else</option>
            </select>
          </p>
          <p class="field"><label for="cf-msg">Message</label><textarea id="cf-msg" name="message" required placeholder="Ask us anything."></textarea></p>
          <p><button class="btn btn--gold" type="submit"><span class="btn__dot"></span>Send message</button></p>
          <p class="form__note">Please don't include sensitive medical details in this form. If your question is clinical, call <a href="tel:1800764763" style="color:var(--blue)">1800&nbsp;764&nbsp;763</a> and speak to the doctor directly.</p>
        </form>
      </div>
    </div>
  </div>
</section>
''' + cta('Rather just book it?',
          'Online booking takes a couple of minutes, and no GP referral is needed.')

    write('contact-us.html',
          'Contact Us | Hobart Vasectomy Centre',
          'Call 1800 SNIPME, email the centre, or send a message. Free phone consultations with the doctor.',
          contact)

    # ====================================================== BOOK ONLINE ====
    book = phero(
        '/assets/generated/23-recovery-home.webp',
        'Booking an appointment from home',
        'Book online',
        'Booked in about <em>two</em> minutes.',
        'The calendar below is the real one. Pick a time that suits, pay the deposit, '
        'and the rest is handled on the day.',
        acts=False
    ) + '''
<section class="section">
  <div class="wrap">
    <div class="split split--wide">
      <div>
        <p class="kicker" data-rev>How it works</p>
        <h2 class="h2" data-rev data-rev-d="1">Four steps, and none of them involve a referral.</h2>
        <div style="margin-top:clamp(28px,3.4vw,42px)" data-rev data-rev-d="2">
          <a class="btn btn--ink" href="''' + BOOK + '''" rel="noopener"><span class="btn__dot"></span>Open the booking calendar</a>
        </div>
        <div class="callout" data-rev data-rev-d="3" style="margin-top:32px;max-width:46ch">
          <p>Not ready to commit? Book a <b>free phone consultation</b> instead and speak to the doctor first &mdash; call <a href="tel:1800764763" style="color:var(--blue)">1800&nbsp;764&nbsp;763</a>.</p>
        </div>
      </div>
      <ol class="tl" data-rev data-rev-d="1">
        <li><span class="tl__y">Step 01</span><div class="tl__c"><b>Pick your time</b><span>The online calendar shows genuine availability at Rosny Park. Choose the slot that suits you.</span></div></li>
        <li><span class="tl__y">Step 02</span><div class="tl__c"><b>Pay the $100 deposit</b><span>That is what holds the appointment. The $730 balance is settled on the day.</span></div></li>
        <li><span class="tl__y">Step 03</span><div class="tl__c"><b>Sign the consent form</b><span>It arrives by SMS three days beforehand. Read it properly &mdash; it lists every risk in full.</span></div></li>
        <li><span class="tl__y">Step 04</span><div class="tl__c"><b>Turn up, once</b><span>Consultation, procedure and discharge all happen in the same visit. You drive yourself home.</span></div></li>
      </ol>
    </div>
  </div>
</section>

<section class="figband">
  <div class="figband__media"><img src="/assets/generated/31-procedure-wide.webp" width="2400" height="1018" alt="The procedure room" loading="lazy" decoding="async"></div>
  <div class="figband__scrim"></div>
  <div class="wrap figband__in">
    <p class="kicker kicker--dk" data-rev>Before you book</p>
    <h2 data-rev data-rev-d="1">Three things worth checking.</h2>
    <ul class="check check--dk" style="margin-top:clamp(28px,3.5vw,44px);max-width:660px" data-rev data-rev-d="2">
      <li>''' + TICK + '''<div><b>Are you on blood thinners?</b><span>Aspirin, warfarin and similar need to stop seven days before. Talk to your GP, or call us first.</span></div></li>
      <li>''' + TICK + '''<div><b>Is your work physical?</b><span>Arrange light duties or time off for the seven days afterwards. We can write a certificate.</span></div></li>
      <li>''' + TICK + '''<div><b>Are you certain?</b><span>A vasectomy is permanent. Reversal is possible, costly, not covered by Medicare, and not always successful.</span></div></li>
    </ul>
  </div>
</section>
''' + cta('The calendar is open.',
          'Pick a time at Rosny Park. A $100 deposit holds it.')

    write('book-online.html',
          'Book Online | Hobart Vasectomy Centre',
          'Book a no-scalpel vasectomy in Hobart online. No GP referral needed, $100 deposit to secure your appointment.',
          book)

    # ============================================================= BLOG ====
    POST_URL = '/blog/why-hobart-men-are-choosing-vasectomy-in-2025'
    blog = phero(
        '/assets/generated/28-hobart-golden.webp',
        'Hobart waterfront at golden hour',
        'Blog',
        'Notes from the <em>clinic</em>.',
        'Plain answers to the questions Tasmanian men actually ask us, written by the '
        'doctors who do the procedure.',
        acts=False
    ) + '''
<section class="section">
  <div class="wrap">
    <div class="postlist">
      <article class="postcard">
        <div class="postcard__media" data-rev>
          <a href="''' + POST_URL + '''"><img src="/assets/generated/28-hobart-golden.webp" width="2400" height="1018" alt="Hobart waterfront at golden hour" loading="lazy" decoding="async"></a>
        </div>
        <div data-rev data-rev-d="1">
          <p class="postcard__meta"><span>24 March 2025</span><span>Dr Geoff Cashion</span><span>Vasectomy</span></p>
          <h2><a href="''' + POST_URL + '''">Why Hobart Men Are Choosing Vasectomy in 2025</a></h2>
          <p>More Tasmanian men are opting for vasectomy than ever before &mdash; and once you look at the alternatives on time, cost and who carries the contraceptive load, it stops being surprising.</p>
          <a class="slide__link" href="''' + POST_URL + '''" style="margin-top:20px">Read the article <span aria-hidden="true">&rarr;</span></a>
        </div>
      </article>
    </div>
  </div>
</section>
''' + cta('Questions the blog did not answer?',
          'Phone consultations are free, and you speak to the doctor who would do the procedure.')

    write('blog/index.html', 'Blog | Hobart Vasectomy Centre',
          'Notes from the clinic, written by the doctors who perform the procedure.', blog)

    # ---------------------------------------------------- the blog post ---
    secs = [
        ('a-10-minute-fix', 'A ten-minute fix to family planning',
         '<p>A vasectomy is one of the simplest medical procedures there is. Our no-scalpel technique takes about ten to fifteen minutes from start to finish. You are in, you are out, and you are back to your day faster than it takes to queue for a flat white on Salamanca Place. No scalpel, no stitches &mdash; a quick procedure under local anaesthetic with minimal discomfort.</p>'),
        ('drive-in-drive-out', 'Drive in, drive out',
         '<p>Worried about needing a lift, or taking days off? Don\'t be. With a no-scalpel vasectomy under local anaesthetic you can drive yourself to and from the appointment. No roping in a mate or your partner to play chauffeur. It is less invasive than a trip to the dentist, and you will be back behind the wheel and heading home &mdash; or even to work &mdash; without missing a beat.</p>'),
        ('affordable', 'Under $600, after Medicare',
         '<p>Cost matters in any medical decision, and this is where vasectomy really separates itself. Your out-of-pocket cost here is <strong>$597</strong> after the Medicare rebate. Compare that with the thousands you would pay a urologist in a private hospital, or the ongoing expense of every other form of contraception, and the maths does itself.</p><p>We submit the Medicare claim for you after the procedure, and the <strong>$233 rebate</strong> is in your account within a day or two. For families watching the budget, it is a one-time cost with a lifetime of savings behind it.</p>'),
        ('better-than-pills', 'Better than pills, IUDs and implants',
         '<p>For years contraception has fallen to women &mdash; the daily admin of the pill, the discomfort of an IUD, the side effects of an implant. Vasectomy flips that. There are no hormonal swings and no doses to forget. No painful insertion, no infection risk, no irregular bleeding, no removal procedure later.</p><p>It is one-and-done: no ongoing appointments, no side effects for your partner, and no more contraceptive burden sitting entirely on her.</p>'),
        ('ditch-the-condoms', 'Ditch the condoms for good',
         '<p>Let\'s be honest &mdash; condoms get old fast. They are inconvenient, they are a recurring cost, and they are not foolproof. A vasectomy lets you stop buying them permanently. After your procedure and the follow-up test that confirms you are clear, that is simply no longer something you think about.</p>'),
        ('expertise-in-hobart', 'World-class expertise, in Hobart',
         '<p>With vasectomy, experience is the variable that matters most. Dr Geoff Cashion, founder of Vasectomy Australia, performs more no-scalpel vasectomies each year than any other doctor in Australia, with more than 15,000 procedures behind him. Dr Matt Valentine has performed over 17,000.</p><p>That is not local expertise being described generously. It is two of the most practised pairs of hands in the country, running clinics ten minutes from the Hobart CBD.</p>'),
        ('making-the-switch', 'Why Hobart men are making the switch',
         '<p>Hobart in 2025 is about practical choices, and vasectomy fits neatly. Whether you are a dad with a full house or a partner ready to take your turn carrying the contraception, it ticks the boxes: quick, affordable, permanent, and done with by lunchtime.</p><p>It is fifteen minutes, and then you stop thinking about it.</p>'),
    ]
    toc = '\n'.join('<li><a href="#%s">%s</a></li>' % (s[0], s[1]) for s in secs)
    body = '\n'.join('<h2 id="%s">%s</h2>\n%s' % (s[0], s[1], s[2]) for s in secs)

    post = '''<section class="phero" data-spine="Blog">
  <div class="phero__media"><img src="/assets/generated/28-hobart-golden.webp" width="2400" height="1018" alt="Hobart waterfront at golden hour" fetchpriority="high"></div>
  <div class="phero__scrim"></div>
  <div class="wrap phero__in">
    <nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">&rsaquo;</span><a href="/blog">Blog</a><span aria-hidden="true">&rsaquo;</span>Article</nav>
    <p class="kicker kicker--dk">24 March 2025 &middot; Dr Geoff Cashion</p>
    <h1>Why Hobart men are choosing vasectomy in <em>2025</em>.</h1>
    <p class="phero__lede">If you are a Hobart dad &mdash; or a Tasmanian man thinking about family planning &mdash; you may have noticed a trend. More blokes are opting for vasectomy than ever before. Here is why.</p>
  </div>
</section>

<section class="section">
  <div class="wrap post">
    <article class="prose" data-rev>''' + body + '''
      <hr style="border:0;border-top:1px solid var(--rule);margin:2.4em 0">
      <p><em>Written by Dr Geoff Cashion, founder of Vasectomy Australia. To book, or to arrange a free phone consultation, call <a href="tel:1800764763">1800&nbsp;764&nbsp;763</a>.</em></p>
    </article>
    <aside class="post__toc" data-rev data-rev-d="1">
      <h2>In this article</h2>
      <ol data-toc>''' + toc + '''</ol>
    </aside>
  </div>
</section>
''' + cta('Ten minutes, and then you stop thinking about it.',
          'Book online at Rosny Park, or call for a free phone consultation first.')

    write('blog/why-hobart-men-are-choosing-vasectomy-in-2025.html',
          'Why Hobart Men Are Choosing Vasectomy in 2025 | Hobart Vasectomy Centre',
          'More Tasmanian men are choosing vasectomy. On time, cost and who carries the contraceptive load, here is why.',
          post)

    # =================================================== PRIVACY POLICY ====
    P = [
      ('collect', 'What personal information we collect, and why',
       '<p>When you register as a patient, your doctor and their support team need to collect your personal information so they can provide you with the best possible healthcare. We also use it for directly related business activities such as financial claims and payments, practice audits, accreditation and normal business processes.</p>'
       '<p>The personal information we collect and hold generally includes:</p><ul>'
       '<li>Your name, address, date of birth and contact details.</li>'
       '<li>Information about your health condition, medical history, social and family history, risk factors, medications, allergies, adverse events, immunisations and treatment you have already received.</li>'
       '<li>Your Medicare number or DVA number, for identification and claiming.</li>'
       '<li>Private health fund details.</li></ul>'
       '<p>Only practice staff who need to see your personal information have access to it. All practice staff have signed a confidentiality agreement as part of their employment contract.</p>'),
      ('how-we-collect', 'How we collect it',
       '<p>We collect your personal information directly &mdash; in person, over the phone, by email, SMS, social media, through this website, or by you completing our online or hard copy forms. When you make your first appointment, our staff collect your personal and demographic information through your registration.</p>'
       '<p>Where it is not possible to collect it from you directly, we may also collect it from your guardian or responsible person; from other healthcare providers involved in your care such as specialists, allied health professionals, hospitals, community health services, pathology and diagnostic imaging services; or from your private health fund, Medicare or DVA.</p>'),
      ('sharing', 'Who we share it with, and when',
       '<p>We may share your personal information with:</p><ul>'
       '<li>Other healthcare providers involved in your care.</li>'
       '<li>Third parties who work with our practice for business purposes, such as IT providers and accreditation agencies.</li>'
       '<li>Bodies to whom we have a statutory requirement to disclose, such as mandatory notification of certain diseases.</li>'
       '<li>Courts, where required or authorised by law, such as under subpoena.</li>'
       '<li>Where necessary to lessen or prevent a serious threat to a patient\'s life, health or safety, or to public health or safety, and it is impractical to obtain consent.</li>'
       '<li>In the course of providing medical services through Electronic Transfer of Prescriptions or the My Health Record system.</li></ul>'
       '<p>We will not use your personal information to market our goods or services to you without your express consent. If you do consent, you can opt out at any time by notifying us in writing.</p>'
       '<p>Other than in the course of providing medical services, or as described in this policy, we will not share your personal information with any third party without your consent. We will not share it with anyone outside Australia &mdash; other than in exceptional circumstances permitted by law &mdash; without your consent.</p>'),
      ('storage', 'How we store and protect it',
       '<p>Your personal information may be held as paper records, electronic records, audio recordings, x-rays, CT scans, videos and photographs.</p>'
       '<p>We store all personal information securely, with protocols to protect it from misuse, loss, interference and unauthorised access:</p><ul>'
       '<li>Electronic records are encrypted and password protected.</li>'
       '<li>Hard copy records are stored in secure locked cabinets.</li>'
       '<li>All staff and contractors sign confidentiality agreements before commencing work with us.</li></ul>'),
      ('access', 'Accessing and correcting your information',
       '<p>You have the right to access and correct the personal information we hold about you, in electronic or hard copy format. We take reasonable steps to correct information that is not accurate or up to date, and will ask you from time to time to verify that what we hold is correct.</p>'
       '<p>To access or correct your information, please put your request in writing to the Practice Manager, Shantelle Bliss, at <a href="mailto:info@vasectomyaustralia.com.au">info@vasectomyaustralia.com.au</a>. Requests are processed within 30 days.</p>'
       '<p>There is no application or processing fee, though you may be charged administration, photocopying or other costs reasonably incurred in fulfilling your request.</p>'),
      ('complaints', 'Making a privacy complaint',
       '<p>If you have concerns about your privacy, or wish to complain about a privacy breach, contact our Practice Manager, Shantelle Bliss, at <a href="mailto:info@vasectomyaustralia.com.au">info@vasectomyaustralia.com.au</a>. Please give us enough detail about your complaint, along with any supporting information.</p>'
       '<p>We will investigate and notify you in writing of the outcome within 30 days of receiving your written complaint. If you are not satisfied with our response you can contact us to discuss it further, or lodge a complaint with the Office of the Australian Information Commissioner at <a href="https://www.oaic.gov.au" rel="noopener" target="_blank">oaic.gov.au</a> or on 1300 363 992.</p>'),
      ('website', 'Privacy and this website',
       '<p>Aside from information you provide yourself in the course of arranging a consultation, this website does not collect or store additional personal information without your consent. That consent is given by acknowledging the cookie notice that loads with the site. If consent is not given, no cookie tracking data is collected.</p>'),
      ('anonymity', 'Dealing with us anonymously',
       '<p>You have the right to deal with us anonymously or under a pseudonym, unless it is impracticable for us to do so, or we are required or authorised by law to deal only with identified individuals.</p>'),
      ('policy-changes', 'Changes to this policy',
       '<p>This policy will be reviewed regularly to make sure it remains consistent with changes in the law, technology and our own operations. Any updated version will be published here.</p>'),
    ]
    pnav = '\n'.join('<li><a href="#%s">%s</a></li>' % (s[0], s[1]) for s in P)
    pbody = '\n'.join('<h2 id="%s">%s</h2>\n%s' % (s[0], s[1], s[2]) for s in P)

    priv = '''<section class="phero" data-spine="Privacy">
  <div class="phero__media"><img src="/assets/generated/27-reception.webp" width="1600" height="893" alt="" loading="lazy" decoding="async"></div>
  <div class="phero__scrim"></div>
  <div class="wrap phero__in">
    ''' + crumb('Privacy policy') + '''
    <h1>How we handle <em>your</em> information.</h1>
    <p class="phero__lede">Vasectomy Australia is committed to managing your personal information in accordance with the Australian Privacy Principles. This explains what we collect, why, and who we share it with.</p>
  </div>
</section>

<section class="section">
  <div class="wrap legal">
    <nav class="legal__nav" aria-label="On this page" data-rev>
      <p class="legal__stamp">Current as of 20 April 2021</p>
      <ol data-toc>''' + pnav + '''</ol>
    </nav>
    <div class="prose" data-rev data-rev-d="1" style="max-width:72ch">''' + pbody + '''</div>
  </div>
</section>
'''
    write('privacy-policy.html', 'Privacy Policy | Hobart Vasectomy Centre',
          'How the Hobart Vasectomy Centre collects, stores, shares and protects your personal information.',
          priv)

    # ========================================================== SITEMAP ====
    links = [
        ('/', 'Home', 'Two vasectomists, 32,000 procedures, $597 out of pocket.'),
        ('/about-us', 'About us', 'Dr Geoff Cashion and Dr Matt Valentine.'),
        ('/patient-information', 'Patient information', 'What happens before, during and after.'),
        ('/vasectomy-fees', 'Vasectomy fees', '$597 out of pocket, and how the Medicare rebate works.'),
        ('/book-online', 'Book online', 'Pick a time at Rosny Park.'),
        ('/location', 'Location', 'Clarence GP Super Clinic, Rosny Park.'),
        ('/contact-us', 'Contact us', 'Phone, email and a message form.'),
        ('/blog', 'Blog', 'Notes from the clinic.'),
        ('/privacy-policy', 'Privacy policy', 'How we handle your information.'),
    ]
    rows = '\n'.join(
        '<li>' + TICK + '<div><b><a href="%s" style="color:var(--ink);text-decoration:none">%s</a></b>'
        '<span>%s</span></div></li>' % (u, t, d) for u, t, d in links)
    sm = '''<section class="phero" data-spine="Sitemap">
  <div class="phero__scrim"></div>
  <div class="wrap phero__in">
    ''' + crumb('Sitemap') + '''
    <h1>Every page, in <em>one</em> place.</h1>
  </div>
</section>
<section class="section">
  <div class="wrap" style="max-width:840px">
    <ul class="check" data-rev>''' + rows + '''</ul>
  </div>
</section>
''' + cta('Looking for something else?', 'Call 1800 SNIPME and ask &mdash; someone will know.')
    write('sitemap.html', 'Sitemap | Hobart Vasectomy Centre',
          'Every page on the Hobart Vasectomy Centre site.', sm)
