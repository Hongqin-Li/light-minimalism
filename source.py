# Generate Documents

import re
import os

os.system('sass light-minimalism.scss docs/light-minimalism.css')
os.system('cp light-minimalism.js docs/light-minimalism.js')
#FIXME
os.system('cp docs/light-minimalism.js fudan.today/src/rebuild/light-minimalism.js')
os.system('cp docs/light-minimalism.css fudan.today/src/rebuild/light-minimalism.css')

template_raw = '{%doc%}'

template = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>

    <link rel="stylesheet" href="light-minimalism.css"/>

    <!-- Font -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat|Rubik&display=swap" rel="stylesheet">

    <!-- Icon -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css" rel="stylesheet">

  </head>

<body class="hmf--dense">

  <script>

    function update_doc(data) {
        // Placeholder for topbar
        document.getElementById("doc-container").innerHTML = data;
        window.scroll({
            top: 0, 
            left: 0, 
            //behavior: 'smooth'
        });
        let a = document.getElementById("menu-trigger--arrow");
        if (a.children[0].checked) 
            a.click();
    } 

    // Update doc template or route to other pages
    // according to current url
    function route() {
        let hash = location.hash;
        if (hash[0] == "#") LM.fetch(location.hash.slice(1), update_doc);
        else LM.fetch("getting-started.html", update_doc);
    }

    // Hide topbar automatically
    let pos = window.pageYOffset;
    window.onscroll = () => {
        let thispos = window.pageYOffset;
        let topbar = document.getElementById("portrait-header");
        if ((topbar.hideable === undefined || topbar.hideable) && pos < thispos && thispos > 3*17)
            topbar.style.transform = "translateY(-3rem)";
        else
            topbar.style.transform = "translateY(0)";
        pos = thispos;
    }

    window.onhashchange = route;
    window.onload = route;

  </script>

  <!-- Landscape Top Bar -->
  <header class="landscape-only">
    <div style="height: 3em; align-items: center;">
      <span>LIGHT-MINIMALISM</span>
      <a class="right-start" 
         style="align-self: flex-end;"
         href="https://github.com/Xinhong-Li/light-minimalism">
        Github
      </a>
    </div>
  </header>

  <!-- Portrait Top Bar -->
  <input type="checkbox" id="menu-trigger" class="hmf--fullscreen-trigger"/>
  <header id="portrait-header" class="portrait-fixed portrait-only" style="top: 0; z-index: 11; width: 100%;"
    ontransitionend="
      if(event.target == this && event.propertyName == 'height') {
        this.hideable = !this.previousElementSibling.checked;
        console.log(this.hideable);
      }"
  >

    <!-- header row 1 -->
    <div style="height: 3em; align-items: center;">
      <span>LIGHT-MINIMALISM</span>
      <label id="menu-trigger--arrow" class="switch--arrow right-start" onclick="
        document.getElementById('menu-trigger').checked = this.children[0].checked;
        this.parentElement.parentElement.hideable = false;
        console.log(this.parentElement.parentElement.hideable);
      ">
        <input type="checkbox"><span></span>
      </label>
    </div>

    <!-- header row 2(dropdown box) -->
    <div style="height: calc(100vh - 3rem); display: block; overflow-y: auto; padding-top: 0;">

    <nav class="nav-menu" style="width: 100%; border: none;">
      {%generate_nav(0)%}
    </nav>

    </div>

  </header>

  <main>

    <!--left menu(optional)-->
    <nav class="nav-menu landscape-only">
      {%generate_nav(1)%}
    </nav>

    <!-- padding for fixed topbar -->
    <div class="mark reveal" id="doc-container" style="--mark-padding--portrait: 3rem 0 0 0;">
      {%doc%}
    </div>

  </main>

  <footer style="background-color: rgba(0, 0, 0, .03);">
    <div class="footer-row" style="justify-content:flex-end;">
      <div class="intro">
        Designed and Built by Xinhong Li<br/>
        Powered by <a>Light Minimalism</a>
      </div>
      <div class="link">
        <a href="https://github.com/Xinhong-Li/light-minimalism">Follow Us</a>
      </div>
    </div>

    <div class="footer-row">
      <div class="intro">Copyright © 2019, Xinhong Li. All rights reserved.</div>
    </div>
  </footer>

</body>
<script type="text/javascript" src="light-minimalism.js"></script>

</html>

'''


srcs = [
  {
    'file': 'docs/index.html',
    'template': template,
    'vars': {
        'doc': ''
    }
  },

  {
    'file': 'docs/getting-started.html',
    'template': template_raw,
    'vars': {
        'doc': r'''

        <h3>Getting Started</h3>

        <p>Download <a href="light-minimalism.css">css</a> and <a href="light-minimalism.js">js</a> file and then include them in html as the boilderplate shown below.</p>

        <pre><code>{%
          syntax_highlight("""

<html>
  <head>

    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>

    <!-- CSS -->
    <link rel="stylesheet" href="light-minimalism.css"/>

    <!-- Optional: Icon -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css" rel="stylesheet">

  </head>

  <body>
    <!-- Contents here -->
  </body>

  <script type="text/javascript" src="light-minimalism.js"></script>
  <!-- Scripts that use LM in light-minimalism.js should be after this -->

</html>


          """)%}</code></pre>

        '''
    }
  },

  {
    'file': 'docs/button.html',
    'template': template_raw,
    'vars': {
        'doc': r'''
        <h3>Button</h3>
       
        <div style="display: flex; flex-wrap: wrap; align-items: center; margin-bottom: 0;">
          <button class="contained" style="margin: 0 2em 2em 0;">CONTAINED</button>
          <button class="light" style="margin: 0 2em 2em 0;">LIGHT</button>
          <button class="outlined" style="margin: 0 2em 2em 0;">OUTLINED</button>
          <button class="text" style="margin: 0 2em 2em 0;">TEXT</button>
        </div>

        <pre><code>{%
          syntax_highlight("""
<button class="contained">CONTAINED</button>
<button class="light">LIGHT</button>
<button class="outlined">OUTLINED</button>
<button class="text">TEXT</button>
          """) 
          %}</code></pre>

        <h3>Icon Button</h3>
        <p>To display icons, we must first add Google's <strong>Material icons</strong> font. For example, add the following tag in <code>{%syntax_highlight('<head></head>')%}</code>.</p>

        <pre><code>{%
        syntax_highlight('<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">')
          %}</code></pre>

        <div style="display: flex; flex-wrap: wrap; align-items: center; margin-bottom: 0;">
          <button class="icon" style="margin: 0 2em 2em 0;"><i class="material-icons">cloud</i></button>
          <button class="icon" style="margin: 0 2em 2em 0;"><i class="material-icons">info</i></button>
          <button class="icon" style="margin: 0 2em 2em 0;"><i class="material-icons">menu</i></button>
        </div>

        <pre><code>{%
          syntax_highlight("""
<button class="icon"><i class="material-icons">cloud</i></button>
<button class="icon"><i class="material-icons">info</i></button>
<button class="icon"><i class="material-icons">menu</i></button>
          """) 
          %}</code></pre>

        <h3>Hybrid Button</h3>

        <div style="display: flex; flex-wrap: wrap; align-items: center; margin-bottom: 0;">
          <button class="contained" style="margin: 0 2em 2em 0;"><i class="material-icons">add</i><span>Add</span></button>
          <button class="light" style="margin: 0 2em 2em 0;"><i class="material-icons">account_circle</i><span>Account</span></button>
          <button class="outlined" style="margin: 0 2em 2em 0;"><i class="material-icons">favorite</i><span>Like</span></button>
          <button class="text" style="margin: 0 2em 2em 0;"><span>Config</span><i class="material-icons">build</i></button>
        </div>

        <pre><code>{%
          syntax_highlight("""
<button class="contained">
  <i class="material-icons">add</i>
  <span>Add</span>
</button>

<button class="light">
  <i class="material-icons">account_circle</i>
  <span>Account</span>
</button>

<button class="outlined">
  <i class="material-icons">favorite</i>
  <span>Like</span>
</button>

<button class="text">
  <span>Config</span>
  <i class="material-icons">build</i>
</button>
          """) 
          %}</code></pre>


        <h3>Customization</h3>

        <p>Disable the button by setting <code><span class="attr">disabled</span></code> attribute.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: flex-end; margin-bottom: 0;">
          <button class="contained" style="margin: 0 2em 2em 0;" disabled>CONTAINED</button>
          <button class="light" style="margin: 0 2em 2em 0;" disabled>LIGHT</button>
          <button class="outlined" style="margin: 0 2em 2em 0;" disabled>OUTLINED</button>
          <button class="text" style="margin: 0 2em 2em 0;" disabled>TEXT</button>
          <button class="icon" style="margin: 0 2em 2em 0;" disabled><i class="material-icons">delete</i></button>

        </div>

        <pre><code>{%
          syntax_highlight("""

<button class="contained" disabled>CONTAINED</button>
<button class="light" disabled>LIGHT</button>
<button class="outlined" disabled>OUTLINED</button>
<button class="text" disabled>TEXT</button>
<button class="icon" disabled><i class="material-icons">delete</i></button>

          """)%}</code></pre>

        <p>Customize size by <code><span class="value">font-size</span></code>.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: flex-end; margin-bottom: 0;">
          <button class="contained" style="font-size: .8em; margin: 0 2rem 2rem 0;">SMALL</button>
          <button class="light" style="font-size: 1em; margin: 0 2rem 2rem 0;">NORMAL</button>
          <button class="outlined" style="font-size: 1.2em; margin: 0 2rem 2rem 0;">LARGE</button>
        </div>

        <pre><code>{%
          syntax_highlight("""

<button class="contained" style="font-size: .8em;">
  SMALL
</button>

<button class="light" style="font-size: 1em;">
  NORMAL
</button>

<button class="outlined" style="font-size: 1.2em;">
  LARGE
</button>

        """)%}</code></pre>

        <p>Customize color by <code><span class="value">color</span></code> or <code><span class="value">background</span></code>.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: flex-end; margin-bottom: 0;">

          <button class="contained" style="background-image: linear-gradient(to right, #ed6ea0 0%, #ec8c69 100%); margin: 0 2rem 2rem 0;">CUSTOMIZED</button>

          <button class="light" style="color: rgba(160, 0, 0, .8); margin: 0 2rem 2rem 0;"><i class="material-icons">favorite</i><span>Favor</span></button>

          <button class="outlined" style="color: rgba(0, 100, 0, .8); margin: 0 2rem 2rem 0;">Save</button>

          <button class="text" style="color: rgba(0, 0, 0, .12); margin: 0 2rem 2rem 0;">Cancel</button>


          <button class="icon" style="color: rgba(255, 255, 255, 1); background-color: rgba(0, 0, 0, .6); margin: 0 2rem 2rem 0;"><i class="material-icons">delete</i></button>

        </div>

        <pre><code>{%
          syntax_highlight("""

<button class="contained"
        style="background-image: linear-gradient(to right, #ed6ea0 0%, #ec8c69 100%);">
  CUSTOMIZED
</button>

<button class="light" style="color: rgba(160, 0, 0, .8);">
  <i class="material-icons">favorite</i>
  <span>Favor</span>
</button>

<button class="outlined" style="color: rgba(0, 100, 0, .8);">
  Save
</button>

<button class="text" style="color: rgba(0, 0, 0, .12);">
  Cancel
</button>

<button class="icon" 
        style="color: rgba(255, 255, 255, 1); 
               background-color: rgba(0, 0, 0, .6);">
  <i class="material-icons">delete</i>
</button>

        """)%}</code></pre>

        '''
    }
  },
  {
    'file': 'docs/toggle-button.html',
    'template': template_raw,
    'vars': {
        'doc': '''

        <h3>Toggle Button</h3>

        <p>A toggle button is a button that represents a setting with two states, such as <code><span class="value">switch</span></code>, <code><span class="value">checkbox</span></code> and <code><span class="value">radio button</span></code>.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: center; margin-bottom: 0;">
          <span class="switch" style="margin: 0 2em 2em 0;">
            <input type="checkbox"/><span></span>
          </span>
          <span class="checkbox" style="margin: 0 2em 2em 0;">
            <input type="checkbox"/><span></span>
          </span>
          <span class="radio" style="margin: 0 2em 2em 0;">
            <input type="radio"/><span></span>
          </span>
          <span class="switch--arrow" style="margin: 0 2em 2em 0;">
            <input type="checkbox"/><span></span>
          </span>
          <span class="switch--menu" style="margin: 0 2em 2em 0;">
            <input type="checkbox"/><span></span>
          </span>
          <label class="switch--heart" style="margin: 0 2em 2em 0;">
            <input type="checkbox"/><span></span>
            <span><i class="material-icons">favorite</i></span>
          </label>
        </div>

        <pre><code>{%
          syntax_highlight("""

<span class="switch">
  <input type="checkbox"><span></span>
</span>

<span class="checkbox">
  <input type="checkbox"><span></span>
</span>

<span class="radio">
  <input type="radio"><span></span>
</span>

<span class="switch--arrow">
  <input type="checkbox"><span></span>
</span>

<span class="switch--menu">
  <input type="checkbox"><span></span>
</span>

<label class="switch--heart">
  <input type="checkbox"/><span></span>
  <span><i class="material-icons">favorite</i></span>
</label>
        """)%}</code></pre>

        <h3>Alignment</h3>

        <p>Wrap toggle buttons by <code><span class="value">list</span></code> to automatically align items inside.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: flex-end; margin-bottom: 0;">

          <div class="list" style="margin: 0 2em 2em 0;">

            <label class="checkbox">
              <span>Single item</span>
              <input type="checkbox"><span></span>
            </label>

            <label class="checkbox">
              <span>Item 1</span>
              <span>Item 2</span>
              <input type="checkbox"><span></span>
            </label>

            <label class="checkbox">
              <span>Left items align to left</span>
              <input type="checkbox"><span></span>
            </label>
          </div>

          <div class="list" style="margin: 0 2em 2em 0;">
            <label class="radio">
              <input type="radio" name="r1"><span></span>
              <span>Item a1</span>
              <span>Item a2</span>
              </label>
            <label class="radio">
              <input type="radio" name="r1"><span></span>
              <span>Item b1</span>
              <span>Item b2</span>
            </label>
            <label class="radio">
              <input type="radio" name="r1"><span></span>
              <span>Right items align to right</span>
            </label>
          </div>

        </div>

        <pre><code>{%
          syntax_highlight("""

<div class="list">

  <label class="checkbox">
    <span>Single item</span>
    <input type="checkbox"><span></span>
  </label>

  <label class="checkbox">
    <span>Item 1</span>
    <span>Item 2</span>
    <input type="checkbox"><span></span>
  </label>

  <label class="checkbox">
    <span>Left items align to left</span>
    <input type="checkbox"><span></span>
  </label>
</div>

<div class="list">

  <label class="radio">
    <input type="radio" name="r1"><span></span>
    <span>Item a1</span>
    <span>Item a2</span>
  </label>

  <label class="radio">
    <input type="radio" name="r1"><span></span>
    <span>Item b1</span>
    <span>Item b2</span>
  </label>

  <label class="radio">
    <input type="radio" name="r1"><span></span>
    <span>Right items align to right</span>
  </label>

</div>

        """)%}</code></pre>

        <h3>Text Event</h3>

        <p>Text will be bound to the toggle button when wrapped in <code><span class="title">&lt;label&gt;</span></code>, unbound in <code><span class="title">&lt;span&gt;</span></code>.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: flex-end; margin-bottom: 0;">

          <div class="list" style="margin: 0 0 2em 0;">
            <label class="switch">
              <span>Clickable text</span>
              <input type="checkbox"><span></span>
            </label>
            <span class="switch">
              <span>Non-clickable text</span>
              <input type="checkbox"><span></span>
            </span>
          </div>

        </div>

        <pre><code>{%
          syntax_highlight("""

<div class="list">

  <label class="switch">
    <span>Clickable text</span>
    <input type="checkbox"><span></span>
  </label>

  <span class="switch">
    <span>Non-clickable text</span>
    <input type="checkbox"><span></span>
  </span>

</div>

        """)%}</code></pre>

        <h3>Customization</h3>

        <p>Customize color of toggle buttons by <code><span class="value">color</span></code>.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: flex-end; margin-bottom: 0;">

          <div class="list" style="margin: 0 0 2em 0;">

            <label class="checkbox" style="color: #f44336;">
              <span>Red</span>
              <input type="checkbox"><span></span>
            </label>
            <label class="radio" style="color: #009688;">
              <span>Teal</span>
              <input type="radio"><span></span>
            </label>
            <label class="switch" style="color: #795548;">
              <span>Brown</span>
              <input type="checkbox"><span></span>
            </label>
          </div>
        </div>

        <pre><code>{%
          syntax_highlight("""

<label class="checkbox" style="color: #f44336;">
  <span>Red</span>
  <input type="checkbox"><span></span>
</label>

<label class="radio" style="color: #009688;">
  <span>Teal</span>
  <input type="radio"><span></span>
</label>

<label class="switch" style="color: #795548;">
  <span>Brown</span>
  <input type="checkbox"><span></span>
</label>
 
        """)%}</code></pre>


        <p>Customize spacing by <code><span class="value" >margin-right</span></code> or <code><span class="value" >width</span></code>.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: flex-end; margin-bottom: 0;">

          <div class="list" style="margin: 0 2em 2em 0;">
            <label class="checkbox">
              <span style="margin-right: 5em;">Item</span>
              <input type="checkbox"><span></span>
            </label>

            <label class="checkbox">
              <input type="checkbox">
              <span class="checkmark" style="margin-right: 5em;"></span>
              <span>Item</span>
            </label>
          </div>

        </div>

        <pre><code>{%
          syntax_highlight("""
<label class="checkbox">
  <span style="margin-right: 5em;">Item</span>
  <input type="checkbox"><span></span>
</label>

<label class="checkbox">
  <input type="checkbox">
  <span class="checkmark" style="margin-right: 5em;"></span>
  <span>Item</span>
</label>
 
        """)%}</code></pre>

        <div class="note">
          <p><strong>NOTE</strong></p>
          <p>When text is on the left side, set <code><span class="value">margin-right</span></code> of right-most text span. Or when text is on the right side, set <code><span class="value">margin-right</span></code> of the <code><span class="value">checkmark</span></code> span. Do not modify <code><span class="value">margin-left</span></code>, since it has been used for alignment by list.</p>
        </div>


        '''
    }
  },

  {'file': 'docs/input.html',
    'template': template_raw,
    'vars': {
        'doc': '''
        <h3>Input</h3>
        
        <div style="display: flex; flex-wrap: wrap; align-items: flex-start; margin-bottom: 0;">

          <span class="input--outlined" style="margin: 0 2em 2em 0;">
            <input type="text" placeholder="This is an outlined input..."/><span></span>
          </span>

          <span class="input--outlined" style="margin: 0 2em 2em 0;
            --background-color: transparent;
            --border-color: #795548;
          ">
            <input type="text" placeholder="Customize background color and border color..."/><span></span>
          </span>

          <span class="input--light" style="margin: 0 2em 2em 0;">
            <input type="text" placeholder="This is an flat input..."/><span></span>
          </span>

          <span class="input--light" style="font-size: 1.2em; margin: 0 2em 2em 0;">
            <input type="text" placeholder="Customize size..."/><span></span>
          </span>

          <span class="input--outlined" style="color: rgba(160, 0, 0, .8); margin: 0 2em 2em 0;">
            <input type="text" placeholder="Customize color..."/><span></span>
          </span>

          <span class="input--light" style="margin: 0 2em 2em 0;">
            <input type="text" placeholder="Customize icon..."/><span></span>
            <i class="material-icons">search</i>
          </span>

          <span class="input--outlined" style="margin: 0 2em 2em 0;">
            <textarea placeholder="This is an outlined textarea..."></textarea><span></span>
          </span>

        </div>

        <pre><code>{%
          syntax_highlight("""
<span class="input--outlined">
  <input type="text" placeholder="This is an outlined input..."/><span></span>
</span>

<span class="input--outlined" style="
  --background-color: transparent;
  --border-color: #795548;
">
  <input type="text" placeholder="Customize background color and border color..."/>
  <span></span>
</span>

<span class="input--light">
  <input type="text" placeholder="This is an flat input..."/><span></span>
</span>

<span class="input--light" style="font-size: 1.2em;">
  <input type="text" placeholder="Customize size..."/><span></span>
</span>

<span class="input--outlined" style="color: rgba(160, 0, 0, .8);">
  <input type="text" placeholder="Customize color..."/><span></span>
</span>

<span class="input--light">
  <input type="text" placeholder="Customize icon..."/><span></span>
  <i class="material-icons">search</i>
</span>

<span class="input--outlined" style="margin: 0 2em 2em 0;">
  <textarea placeholder="This is an outlined textarea..."></textarea><span></span>
</span>


        """)%}</code></pre>

         
        <h3>Input Bar</h3>

        <p>This can be a search bar.</p>

        <div>
          <div class="inputbar" style="width: 100%; background: white;">
            <input type="text" placeholder="Please input sth...">
            <span style="--width: 5em;"><span>Send</span></span>
          </div>
        </div>

        <pre><code>{%
          syntax_highlight("""
<div class="inputbar" style="width: 100%; background: white;">
    <input type="text" placeholder="Please input sth...">
    <span style="--width: 5em;"><span>Send</span></span>
</div>
        """)%}</code></pre>

          <div class="note" style="">
            <p><strong>NOTE</strong></p>
            <p>Remember to specify the width of both the whole input bar and tag, as <code><span class="value">"width: 100%;"</span></code> and <code><span class="value">"--width: 5em"</span></code> above.</p>
          </div>


        '''}},

  { 'file': 'docs/dialog.html',
    'template': template_raw,
    'vars': {
        'doc': '''

        <h3>Dialog</h3>

        <div>

        <input type="checkbox" for="idialog-trigger"/>

        <input class="dialog-trigger" id="idialog-trigger" type="checkbox"/>
        <div class="dialog-container frosted-glass" style="z-index: 12; background-color: white;">
          <div class="dialog-content">

            <div class="mark">
              <h3>Hello!</h3>
              <p>This is a dialog.</p>
            </div>

            <!-- Action buttons -->
            <div style="text-align: right;">
              <label for="dialog-trigger" style="align-self: flex-end;"><a class="icon"><i class="material-icons">navigate_before</i></a></label>
            </div>
          </div>
        </div>
        
        </div>



        '''}},

  { 'file': 'docs/select.html',
    'template': template_raw,
    'vars': {
        'doc': '''

        <h3>Select</h3>

        <div style="display: flex; margin-bottom: 0; flex-wrap: wrap; align-items: flex-start; z-index: 1;">
          <button class="select" style="margin: 0 2em 2em 0;">
            <div>Fruits</div>
            <div>
              <div>
                <label><input type="radio" name="sel"><span>Apple</span></label>
                <label><input type="radio" name="sel"><span>Orange</span></label>
                <label><input type="radio" name="sel"><span>Banana</span></label>
                <label><input type="radio" name="sel"><span>Pear</span></label>
                <label><input type="radio" name="sel"><span>Pinapple</span></label>
              </div>
            </div>
          </button>

          <button class="select" style="margin: 0 2em 2em 0;">
            <input type="text" placeholder="Fruits">
            <div>
              <div>
                <label><input type="radio" name="sel"><span>Apple</span></label>
                <label><input type="radio" name="sel"><span>Orange</span></label>
                <label><input type="radio" name="sel"><span>Banana</span></label>
                <label><input type="radio" name="sel"><span>Pear</span></label>
                <label><input type="radio" name="sel"><span>Pinapple</span></label>
              </div>
            </div>
          </button>

        </div>

        <pre><code>{%
          syntax_highlight("""
<button class="select" style="--nslots: 3;">
<!-- nslots defines the dropdown height by slots, whose default value is 3. -->
  <div>Fruits</div>
  <div>
    <div>
      <label><input type="radio" name="sel"><span>Apple</span></label>
      <label><input type="radio" name="sel"><span>Orange</span></label>
      <label><input type="radio" name="sel"><span>Banana</span></label>
      <label><input type="radio" name="sel"><span>Pear</span></label>
      <label><input type="radio" name="sel"><span>Pinapple</span></label>
    </div>
  </div>
</div>
 
<button class="select">
  <input type="text" placeholder="Fruits">
  <div>
    <div>
      <label><input type="radio" name="sel"><span>Apple</span></label>
      <label><input type="radio" name="sel"><span>Orange</span></label>
      <label><input type="radio" name="sel"><span>Banana</span></label>
      <label><input type="radio" name="sel"><span>Pear</span></label>
      <label><input type="radio" name="sel"><span>Pinapple</span></label>
    </div>
  </div>
</button>

        """)%}</code></pre>

        <h3>Tags</h3>

        <div style="display: flex; margin-bottom: 0; flex-wrap: wrap; align-items: flex-start; z-index: 1;">
          <button class="select" style="margin: 0 2em 2em 0;">
            <div class="tag-container">
              <label><input type="checkbox"><span>Apple</span></label>
              <label><input type="checkbox"><span>Pinapple</span></label>
            </div>
            <div>
              <div>
                <label><input type="checkbox"><span>Apple</span></label>
                <label><input type="checkbox"><span>Orange</span></label>
                <label><input type="checkbox"><span>Banana</span></label>
                <label><input type="checkbox"><span>Pear</span></label>
                <label><input type="checkbox"><span>Pinapple</span></label>
              </div>
            </div>
          </button>
        </div>

        <pre><code>{%
          syntax_highlight("""

<button class="select">
  <div class="tag-container">
    <label><input type="checkbox"><span>Apple</span></label>
    <label><input type="checkbox"><span>Pinapple</span></label>
  </div>
  <div>
    <div>
      <label><input type="checkbox"><span>Apple</span></label>
      <label><input type="checkbox"><span>Orange</span></label>
      <label><input type="checkbox"><span>Banana</span></label>
      <label><input type="checkbox"><span>Pear</span></label>
      <label><input type="checkbox"><span>Pinapple</span></label>
    </div>
  </div>
</button>
 
        """)%}</code></pre>

        
        '''}},


  { 'file': 'docs/toast.html',
    'template': template_raw,
    'vars': {
        'doc': '''

        <h3>Toast</h3>

        <div>
            <button class="light" onclick="LM.toast('Hello')">Click to toast!</button>
        </div>

        <pre><code>{%
          syntax_highlight("""

<button class="light" 
        onclick="LM.toast('Hello');">
    Click to toast!
</button>

        """)%}</code></pre>


        
        '''}},


  { 'file': 'docs/card.html',
    'template': template_raw,
    'vars': {
        'doc': '''

        <h3>Card</h3>

        <p>Card groups its contents and prettify our page. Customized card can be used in chat message UI.</p>

        <div style="margin-bottom: 0;">
          <div class="card" style="margin: 0 2rem 2rem 0">Default card</div>
          <div class="card--outlined" style="margin: 0 2rem 2rem 0;">Outlined card</div>
          <div class="card--flat" style="color: white; background-color: rgba(0, 0, 0, .8); margin: 0 2rem 2rem 0; ">Flat card</div>
          <div class="card--outlined" style="border-radius: 1em 1em 0 1em; margin: 0 2rem 2rem 0;">Customize border radius</div>
          <div class="card--outlined" style="
            border: 1px solid rgba(160, 0, 0, .12);
            color: rgba(160, 0, 0, .8);
            background-color: rgba(160, 0, 0, .04);
            margin: 0 2rem 2rem 0; ">Customize color</div>

        </div>

        <pre><code>{%
          syntax_highlight("""
<div class="card">Default card</div>
<div class="card--outlined">Outlined card</div>
<div class="card--flat" 
     style="color: white; 
            background-color: rgba(0, 0, 0, .8);">
  Flat card</div>

<div class="card--outlined" 
     style="border-radius: 1em 1em 0 1em;">
  Customize border radius</div>

<div class="card--outlined" 
     style="border: 1px solid rgba(160, 0, 0, .12);
            color: rgba(160, 0, 0, .8);
            background-color: rgba(160, 0, 0, .04);">
  Customize color</div>

        """)%}</code></pre>


        '''}},
  {
    'file': 'docs/rating.html',
    'template': template_raw,
    'vars': {
        'doc': r'''
        <h3>Rating</h3>

        <div style="margin-bottom: 0;">
          <svg xmlns="http://www.w3.org/2000/svg" style="display: none">
            <symbol id="star" viewBox="-2 -2 30 30">
                <path d="M26 10.109c0 .281-.203.547-.406.75l-5.672 5.531 1.344 7.812c.016.109.016.203.016.313 0 .406-.187.781-.641.781a1.27 1.27 0 0 1-.625-.187L13 21.422l-7.016 3.687c-.203.109-.406.187-.625.187-.453 0-.656-.375-.656-.781 0-.109.016-.203.031-.313l1.344-7.812L.39 10.859c-.187-.203-.391-.469-.391-.75 0-.469.484-.656.875-.719l7.844-1.141 3.516-7.109c.141-.297.406-.641.766-.641s.625.344.766.641l3.516 7.109 7.844 1.141c.375.063.875.25.875.719z"/>
            </symbol>
          </svg>

          <span class="rating" style="margin: 0 2rem 2rem 0;">
            <input type="radio" name="str1" id="s11"/><label for="s11"><svg><use xlink:href="#star"></use></svg></label>
            <input type="radio" name="str1" id="s12"/><label for="s12"><svg><use xlink:href="#star"></use></svg></label>
            <input type="radio" name="str1" id="s13"/><label for="s13"><svg><use xlink:href="#star"></use></svg></label>
            <input type="radio" name="str1" id="s14"/><label for="s14"><svg><use xlink:href="#star"></use></svg></label>
            <input type="radio" name="str1" id="s15"/><label for="s15"><svg><use xlink:href="#star"></use></svg></label>
          </span>

          <span class="rating" style="margin: 0 2rem 2rem 0; color: white; 
            --fill-color: white;
            --fill-color--inactive: #ddd;
            --border-color: #aaa;
            --border-color--inactive: #ddd;
            --border-width: 1px;
            --border-width--inactive: 1px;">
            <input type="radio" name="str2" id="s21"/><label for="s21"><svg><use xlink:href="#star"></use></svg></label>
            <input type="radio" name="str2" id="s22"/><label for="s22"><svg><use xlink:href="#star"></use></svg></label>
            <input type="radio" name="str2" id="s23"/><label for="s23"><svg><use xlink:href="#star"></use></svg></label>
            <input type="radio" name="str2" id="s24"/><label for="s24"><svg><use xlink:href="#star"></use></svg></label>
            <input type="radio" name="str2" id="s25"/><label for="s25"><svg><use xlink:href="#star"></use></svg></label>
          </span>

        </div>

        <pre><code>{%
          syntax_highlight("""

<svg xmlns="http://www.w3.org/2000/svg" style="display: none">
  <symbol id="star" viewBox="-2 -2 30 30">
      <path d="M26 10.109c0 .281-.203.547-.406.75l-5.672 5.531 1.344 7.812c.016.109.016.203.016.313 0 .406-.187.781-.641.781a1.27 1.27 0 0 1-.625-.187L13 21.422l-7.016 3.687c-.203.109-.406.187-.625.187-.453 0-.656-.375-.656-.781 0-.109.016-.203.031-.313l1.344-7.812L.39 10.859c-.187-.203-.391-.469-.391-.75 0-.469.484-.656.875-.719l7.844-1.141 3.516-7.109c.141-.297.406-.641.766-.641s.625.344.766.641l3.516 7.109 7.844 1.141c.375.063.875.25.875.719z"/>
  </symbol>
</svg>

<span class="rating">
  <input type="radio" name="str1" id="s11"/><label for="s11"><svg><use xlink:href="#star"></use></svg></label>
  <input type="radio" name="str1" id="s12"/><label for="s12"><svg><use xlink:href="#star"></use></svg></label>
  <input type="radio" name="str1" id="s13"/><label for="s13"><svg><use xlink:href="#star"></use></svg></label>
  <input type="radio" name="str1" id="s14"/><label for="s14"><svg><use xlink:href="#star"></use></svg></label>
  <input type="radio" name="str1" id="s15"/><label for="s15"><svg><use xlink:href="#star"></use></svg></label>
</span>

<span class="rating" style="
  --fill-color: white;
  --fill-color--inactive: #ddd;
  --border-color: #aaa;
  --border-color--inactive: #ddd;
  --border-width: 1px;
  --border-width--inactive: 1px;">
  <input type="radio" name="str2" id="s21"/><label for="s21"><svg><use xlink:href="#star"></use></svg></label>
  <input type="radio" name="str2" id="s22"/><label for="s22"><svg><use xlink:href="#star"></use></svg></label>
  <input type="radio" name="str2" id="s23"/><label for="s23"><svg><use xlink:href="#star"></use></svg></label>
  <input type="radio" name="str2" id="s24"/><label for="s24"><svg><use xlink:href="#star"></use></svg></label>
  <input type="radio" name="str2" id="s25"/><label for="s25"><svg><use xlink:href="#star"></use></svg></label>
</span>

        """)%}</code></pre>

        '''}},
  {
    'file': 'docs/svg.html',
    'template': template_raw,
    'vars': {
        'doc': r'''
        <h3>SVG</h3>

        <div style="margin-bottom: 0; display: flex;">
          <svg xmlns="http://www.w3.org/2000/svg" style="display: none">
            <symbol id="star" viewBox="-2 -2 30 30">
                <path d="M26 10.109c0 .281-.203.547-.406.75l-5.672 5.531 1.344 7.812c.016.109.016.203.016.313 0 .406-.187.781-.641.781a1.27 1.27 0 0 1-.625-.187L13 21.422l-7.016 3.687c-.203.109-.406.187-.625.187-.453 0-.656-.375-.656-.781 0-.109.016-.203.031-.313l1.344-7.812L.39 10.859c-.187-.203-.391-.469-.391-.75 0-.469.484-.656.875-.719l7.844-1.141 3.516-7.109c.141-.297.406-.641.766-.641s.625.344.766.641l3.516 7.109 7.844 1.141c.375.063.875.25.875.719z"/>
            </symbol>
          </svg>

          <svg xmlns="http://www.w3.org/2000/svg" style="display: none">
            <symbol id="comment" viewBox="0 0 512 512">
              <path d="M394.768,137.928c4.32,0,7.968,3.648,7.968,7.968v176.616c0,4.32-3.648,7.968-7.968,7.968h-50.464H327.04v17.264v39.776  l-66.568-53.256l-4.728-3.784h-6.056H117.232c-4.32,0-7.968-3.648-7.968-7.968V145.896c0-4.32,3.648-7.968,7.968-7.968H394.768   M394.768,120.664H117.232c-13.88,0-25.232,11.352-25.232,25.232v176.616c0,13.88,11.352,25.232,25.232,25.232h132.464  l94.616,75.696v-75.696h50.464c13.88,0,25.232-11.352,25.232-25.232V145.896C420,132.016,408.648,120.664,394.768,120.664  L394.768,120.664z"/>
            </symbol>
          </svg>

          <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <symbol id="edit" viewBox="0 0 24 24">
              <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/>
              <path d="M0 0h24v24H0z" fill="none"/>
            </symbol>
          </svg>

          <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <symbol id="pencil" viewBox="0 0 235.937 235.937">
              <g>
                <g>
                  <g>
                    <g>
                      <path style="fill: var(--border, #2D213F);" d="M224.248,20.622c15.586,15.554,15.586,40.896,0,56.45L87.969,213.351      c-0.982,0.982-2.217,1.679-3.548,2.059l-74.317,20.242c-0.697,0.19-1.394,0.285-2.091,0.285c-2.091,0-4.15-0.824-5.67-2.344      c-2.027-2.027-2.819-5.005-2.059-7.761l20.242-74.285c0.38-1.362,1.077-2.598,2.059-3.58l136.31-136.279      C166.436,4.15,176.446,0,187.121,0c10.644,0,20.686,4.15,28.225,11.689L224.248,20.622z M216.645,60.727      c5.259-9.155,4.055-20.971-3.738-28.764l-8.902-8.933c-4.53-4.498-10.517-7.001-16.884-7.001c-4.277,0-8.363,1.14-11.943,3.231      L216.645,60.727z M200.996,77.674l4.973-4.973l-42.702-42.702l-4.973,4.973L200.996,77.674z M80.905,197.734l108.75-108.75      l-5.829-5.797L77.896,189.118L80.905,197.734z M65.193,179.139L172.518,71.846l-8.3-8.3l-107.832,107.8l1.869,5.385      L65.193,179.139z M47.421,157.661L152.877,52.205l-5.924-5.924L38.647,154.589L47.421,157.661z M66.048,203.784l-2.946-8.395      l-13.78-4.815c-2.312-0.792-4.118-2.629-4.91-4.91l-4.815-13.748l-7.318-2.566l-11.182,41.086l4.403,4.403L66.048,203.784z"/>
                      <path style="fill: var(--eraser, #EAEEEF);" d="M212.907,31.963c7.793,7.793,8.997,19.609,3.738,28.764L175.179,19.26      c3.58-2.091,7.666-3.231,11.943-3.231c6.367,0,12.354,2.503,16.884,7.001L212.907,31.963z"/>
                      <path style="fill: var(--secondary, #FEDE94);" d="M205.969,72.701l-4.972,4.972l-42.702-42.702l4.972-4.972L205.969,72.701z"/>
                      <path style="fill: var(--secondary, #FEDE94);" d="M189.656,88.983L80.905,197.734l-3.009-8.616L183.827,83.186L189.656,88.983z"/>
                      <path style="fill: var(--primary, #F47C6D);" d="M172.518,71.846L65.193,179.139l-6.938-2.408l-1.869-5.385l107.832-107.8L172.518,71.846z"/>
                      <path style="fill: var(--secondary, #FEDE94);" d="M152.877,52.205L47.421,157.661l-8.774-3.072L146.954,46.282L152.877,52.205z"/>
                      <path style="fill: var(--secondary, #FEDE94);" d="M63.102,195.39l2.946,8.395L25.5,214.84l-4.403-4.403l11.182-41.086l7.318,2.566l4.815,13.748      c0.792,2.281,2.598,4.118,4.91,4.91L63.102,195.39z"/>
                    </g>
                  </g>
                  <path style="fill: rgba(0, 0, 0, .15);" d="M198.164,18.747c-3.374-1.768-7.134-2.718-11.043-2.718c-4.277,0-8.363,1.14-11.943,3.231    l30.541,30.541C193.767,32.986,195.614,23.309,198.164,18.747z"/>
                </g>
              </g>
            </symbol>
          </svg>

          <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <symbol id="pencil--flat" viewBox="0 0 23 23">
              <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                <g id="Full-Color" transform="translate(-451.000000, -151.000000)">
                  <g id="pencil" transform="translate(450.000000, 151.000000)">
                    <path fill="var(--primary, #FFCC00)" d="M1.5,22.5 L3.493,15.525 L18.226,0.792 C18.615,0.403 19.246,0.403 19.635,0.792 L23.208,4.365 C23.597,4.754 23.597,5.385 23.208,5.774 L8.475,20.507 L1.5,22.5 Z"/>
                    <polygon fill="var(--secondary, #FFFFFF)" points="8.4902 20.4902 8.4802 20.5102 1.5002 22.5002 3.4902 15.5202 3.5102 15.5102"/>
                    <path fill="var(--eraser, #FF2C55)" d="M23.21,5.77 L21.99,6.99 L17.01,2.01 L18.23,0.79 C18.62,0.4 19.25,0.4 19.64,0.79 L23.21,4.36 C23.6,4.75 23.6,5.38 23.21,5.77"/>
                    <path d="M22.5590466,3.71574661 C22.7543088,3.52048446 23.0708912,3.52048446 23.2661534,3.71574661 L23.5611534,4.01074661 C24.1464155,4.59600876 24.1464155,5.54259124 23.5611414,6.12786539 L8.82814139,20.8598654 C8.76807719,20.9199255 8.69370239,20.9636938 8.61203339,20.9870412 L1.63703339,22.9810412 C1.25986726,23.0888647 0.911100702,22.7401933 1.01882137,22.3629977 L1.64082137,20.1849977 C1.68826643,20.0188638 1.81812023,19.8889969 1.98424943,19.8415352 L8.21266542,18.0621278 L22.5590466,3.71574661 Z" fill="var(--shadow, rgba(0, 0, 0, 0.24))"/>
                    <path d="M1.5,22.5 L3.493,15.525 L18.226,0.792 C18.615,0.403 19.246,0.403 19.635,0.792 L23.208,4.365 C23.597,4.754 23.597,5.385 23.208,5.774 L8.475,20.507 L1.5,22.5 Z" stroke="var(--border, #000000)" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M21.9902,6.9902 L17.0102,2.0102" stroke="var(--border, #000000)" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M8.4902,20.4902 L3.5102,15.5102" stroke="var(--border, #000000)" stroke-linecap="round" stroke-linejoin="round"/>
                  </g>
                </g>
              </g>
            </symbol>
          </svg>

          <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <symbol id="fav" viewBox="0 0 368 368">
              <g transform="translate(22 25)">
                <path style="fill: var(--fill, #FF793B);" d="M-14,112.727c0-96.4,99.6-153.2,157.6-85.2c9.6,11.2,27.2,11.2,36.8,0   c58-68.4,157.6-11.2,157.6,85.2c0,90-85.6,143.6-158.4,201.6c-10.4,8-24.8,8-35.2,0C71.6,256.327-14,202.327-14,112.727   L-14,112.727z"/>
                <path style="fill: rgba(0, 0, 0, .06);" d="M216.8,1.527c55.6-19.6,121.2,32.8,121.2,111.2c0,90-162.8,212-173.2,204   C280,177.927,338,89.527,216.8,1.527z"/>
                <g>
                  <path style="fill: var(--border, #C6490F);" d="M162,328.327c-8,0-16-2.4-22.4-7.6c-8.8-7.2-17.6-14-26.8-20.8c-66.4-51.2-134.8-104.4-134.8-187.2    c0-53.6,30-100.8,74.8-117.6c35.2-12.8,71.6-2.8,96.8,27.2c3.2,3.6,7.6,5.6,12.4,5.6s9.2-2,12.4-5.6c25.6-30,61.6-40,96.8-27.2    c44.8,16.4,74.8,63.6,74.8,117.6c0,82.8-68.4,135.6-134.4,186.8c-9.2,7.2-18,14-27.2,21.2C178,325.927,170,328.327,162,328.327z     M83.2,5.527c-8,0-16.4,1.6-24.8,4.8C26,21.927-6,58.327-6,112.727c0,74.8,65.6,125.6,128.8,174.4c8.8,6.8,18,14,26.8,20.8    c7.2,5.6,18,5.6,25.2,0c8.8-7.2,18-14,27.2-21.2c66-50.8,128-99.2,128-174c0-54.4-32.4-90.8-64.4-102.8    c-29.2-10.8-58-2.4-79.2,22.8c-6,7.2-15.2,11.2-24.4,11.2s-18.4-4-24.4-11.2C122.4,15.127,103.2,5.527,83.2,5.527z"/>
                  <path style="fill: var(--border, #C6490F);" d="M106,232.327c-1.6,0-3.6-0.4-4.8-1.6c-27.6-22-46-40.4-59.2-58.8c-2.4-3.6-1.6-8.4,2-11.2    c3.6-2.4,8.4-1.6,11.2,2c12.4,17.2,29.6,34.4,56,55.6c3.6,2.8,4,7.6,1.2,11.2C110.4,231.527,108.4,232.327,106,232.327z     M31.2,138.727c-3.6,0-6.8-2.4-7.6-6c-1.6-6-2.4-12-3.6-18.4c-0.4-4.4,2.4-8.4,6.8-8.8s8.4,2.4,8.8,6.8c0.8,6,1.6,11.2,2.8,16    c1.2,4.4-1.2,8.8-5.6,10C32.4,138.727,32,138.727,31.2,138.727z"/>
                </g>
              </g>
            </symbol>
          </svg>

          <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <symbol id="heart--flat" viewBox="0 0 25 23">
              <g fill-rule="evenodd" fill="none" stroke-width="1" stroke="none">
                <g transform="translate(-300.000000, -101.000000)">
                  <g transform="translate(300.000000, 101.000000)">
                    <path d="M24.5,7 C24.5,3.41 21.59,0.5 18,0.5 C15.681,0.5 13.65,1.719 12.5,3.547 C11.35,1.719 9.319,0.5 7,0.5 C3.41,0.5 0.5,3.41 0.5,7 C0.5,7.169 0.513,7.334 0.525,7.5 L0.5,7.5 C0.5,16.5 11.5,22.5 12.5,22.5 C13.5,22.5 24.5,16.5 24.5,7.5 L24.475,7.5 C24.487,7.334 24.5,7.169 24.5,7" fill="var(--fill, #FF2C55)"/>
                    <path d="M-0.0002,7.0002 C-0.0002,6.7695512 0.0118609344,6.53610512 0.0351901669,6.29836913 C0.0948520269,5.69038637 0.98454279,5.6997967 1.03133137,6.3089054 C1.30920064,9.92629665 3.42292338,13.3148708 6.73061013,16.2471793 C8.97779027,18.2393346 11.9525171,20.0002 12.4998,20.0002 C13.0470829,20.0002 16.0218097,18.2393346 18.2689899,16.2471793 C21.5766766,13.3148708 23.6903994,9.92629665 23.9682686,6.3089054 C24.0150678,5.69965848 24.9050314,5.69044645 24.9644319,6.2985941 C24.9877475,6.53730178 24.9998,6.77058476 24.9998,7.0002 C24.9998,7.12130537 24.9954041,7.22990126 24.985131,7.37948746 C24.9947145,7.41814554 24.9998,7.45857888 24.9998,7.5002 C24.9998,11.6373125 22.8124471,15.4570184 19.2119347,18.7444427 C16.7287351,21.0117119 13.4145883,23.0002 12.4998,23.0002 C11.5850117,23.0002 8.27086491,21.0117119 5.78766532,18.7444427 C2.18715294,15.4570184 -0.0002,11.6373125 -0.0002,7.5002 C-0.0002,7.4577332 0.00509425482,7.41650294 0.0150587451,7.37713324 C0.00473433441,7.23044282 -0.0002,7.11771542 -0.0002,7.0002 Z" fill="var(--shadow, rgba(0, 0, 0, 0.24))" fill-rule="nonzero"/>
                    <path d="M24.5,7 C24.5,3.41 21.59,0.5 18,0.5 C15.681,0.5 13.65,1.719 12.5,3.547 C11.35,1.719 9.319,0.5 7,0.5 C3.41,0.5 0.5,3.41 0.5,7 C0.5,7.169 0.513,7.334 0.525,7.5 L0.5,7.5 C0.5,16.5 11.5,22.5 12.5,22.5 C13.5,22.5 24.5,16.5 24.5,7.5 L24.475,7.5 C24.487,7.334 24.5,7.169 24.5,7 Z" stroke="var(--border, #000000)" stroke-linecap="round" stroke-linejoin="round"/>
                  </g>
                </g>
              </g>
            </symbol>
          </svg>

          <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <symbol id="msg--flat" viewBox="0 0 25 25">
              <g transform="translate(-1, 0)" fill="none">
                <path d="M13.5,0.5 C6.873,0.5 1.5,5.425 1.5,11.5 C1.5,13.376 2.019,15.138 2.925,16.682 C3.519,17.692 3.589,18.929 3.178,20.026 L1.5,24.5 L7.395,22.143 C8.225,21.811 9.137,21.779 9.998,22.021 C11.105,22.332 12.281,22.5 13.5,22.5 C20.127,22.5 25.5,17.575 25.5,11.5 C25.5,5.425 20.127,0.5 13.5,0.5" fill="var(--fill, #4CD964)"/>
                <path d="M24.9472073,10.4509953 C25.0063834,9.85012176 25.8822402,9.84946412 25.9423186,10.4502481 C25.9801927,10.8289888 25.9998,11.1681703 25.9998,11.5 C25.9998,17.8615485 20.3944512,23 13.4998,23 C12.2547276,23 11.0337136,22.8310891 9.86250816,22.5023482 C9.09366879,22.2862517 8.29554279,22.3212194 7.58042744,22.6072655 L1.68542744,24.9642655 C1.28203758,25.125553 0.879039955,24.7310714 1.0316763,24.3243293 L1.9146763,21.9713293 C1.9640754,21.8396916 2.06661626,21.7349362 2.19716855,21.6827361 L7.20910466,19.6787617 C8.13171855,19.3097161 9.15543989,19.2648646 10.1329211,19.5396038 C11.2162045,19.8436662 12.346302,20 13.4998,20 C19.4688435,20 24.4175644,15.8289807 24.9472073,10.4509953 Z M2.49379388,16.9354437 C1.51859008,15.2735074 0.9998,13.4203807 0.9998,11.5 C0.9998,11.1111848 1.02130157,10.7231077 1.06377566,10.3355316 C1.12954999,9.73534081 2.00536817,9.74431093 2.05883569,10.345723 C2.18878369,11.8074009 2.6296376,13.1918749 3.35586804,14.4286616 C3.92495229,15.3969871 4.06328046,16.5674334 3.77772522,17.7038505 C3.65251307,18.2021541 2.94730744,18.2101874 2.81077639,17.7148655 C2.72808955,17.4148853 2.62583849,17.1599986 2.49379388,16.9354437 Z" fill="var(--shadow, rgba(0, 0, 0, 0.24))"/>
                <path d="M13.5,0.5 C6.873,0.5 1.5,5.425 1.5,11.5 C1.5,13.376 2.019,15.138 2.925,16.682 C3.519,17.692 3.589,18.929 3.178,20.026 L1.5,24.5 L7.395,22.143 C8.225,21.811 9.137,21.779 9.998,22.021 C11.105,22.332 12.281,22.5 13.5,22.5 C20.127,22.5 25.5,17.575 25.5,11.5 C25.5,5.425 20.127,0.5 13.5,0.5 Z" stroke="var(--border, #000000)" stroke-linecap="round" stroke-linejoin="round"/>
              </g>
            </symbol>
          </svg>

          <!--label class="switch--comment" style="margin: 0 2rem 2rem 0;">
            <svg><use xlink:href="#comment"></use></svg>
            <input type="checkbox"/><span></span>
          </label-->

          <label class="switch--edit" style="margin: 0 2rem 2rem 0; color: #4e342e;">
            <input type="checkbox"/><span></span>
            <svg><use xlink:href="#pencil"></use></svg>
          </label>

          <label class="switch--heart" style="margin: 0 2rem 2rem 0;">
            <input type="checkbox"/><span></span>
            <svg style="font-size: 1em;"><use xlink:href="#fav"></use></svg>
          </label>

          <label class="switch--edit" style="margin: 0 2rem 2rem 0;">
            <input type="checkbox"/><span></span>
            <svg style="
              font-size: 1em;
              /*
              --primary-color: ;
              --secondary-color: ;
              --eraser-color: ;
              --fill-color: #f54b55;
              --shadow-color: transparent;
              --border-color: transparent;
              --fill-color--inactive: #f54b55;
              --shadow-color--inactive: transparent;
              --border-color--inactive: transparent;
              */
            ">
              <use xlink:href="#pencil--flat"></use>
            </svg>
          </label>

          <label class="switch--heart" style="margin: 0 2rem 2rem 0;">
            <input type="checkbox"/><span></span>
            <svg style="/*
              --fill-color: #f54b55;
              --shadow-color: transparent;
              --border-color: transparent;
              --fill-color--inactive: #f54b55;
              --shadow-color--inactive: transparent;
              --border-color--inactive: transparent;
            */">
              <use xlink:href="#heart--flat"></use>
            </svg>
          </label>

          <label class="switch--msg" style="margin: 0 2rem 2rem 0;">
            <input type="checkbox"/><span></span>
            <svg style="font-size: 1em;"><use xlink:href="#msg--flat"></use></svg>
          </label>


        </div>

        <!--pre><code>{%
          syntax_highlight("""

        """)%}</code></pre-->


        '''}},




  {
    'file': 'docs/mark.html',
    'template': template_raw,
    'vars': {
        'doc': r'''

        <h3>Mark</h3>

        <p>The <code><span class="value">mark</span></code> container is quite suitable for text-based articles.</p>


          <h1>h1</h1>
          <h2>h2</h2>
          <h3>h3</h3>
          <h4>h4</h4>
          <h5>h5</h5>
          <h6>h6</h6>
          <p>Paragraph</p>
          <p><strong>Bold Text</strong></p>
          <p><a>Link</a></p>

          <div class="note">
            <p><strong>NOTE</strong></p>
            <p>This is a note.</p>
          </div>

          <div class="blocklist">
            <div>This is a block list.</div>
            <div>It's responsive.</div>
            <div>This is a customized <a class="link" style="--opacity: .8; --opacity--hover: .6;">link</a></div>
          </div>

          <div class="blocklist--striped" style="--primary-color: rgba(0, 0, 0, .04); --secondary-color: transparent;">
            <div>This is a block list.</div>
            <div>It's responsive.</div>
            <div>Color can be customized by --primary-color and --secondary-color.</div>
          </div>
        
        <pre><code>{%
          syntax_highlight("""

<div class="mark">

  <h1>h1</h1>
  <h2>h2</h2>
  <h3>h3</h3>
  <h4>h4</h4>
  <h5>h5</h5>
  <h6>h6</h6>

  <p>Paragraph</p>

  <p><strong>Bold Text</strong></p>

  <p><a>Link</a></p>

  <div class="note">
    <p><strong>NOTE</strong></p>
    <p>This is a note.</p>
  </div>

  <div class="blocklist">
    <div>This is a block list.</div>
    <div>It's responsive.</div>
    <div>This is a customized <a class="link" style="--opacity: .8; --opacity--hover: .6;">link</a></div>
  </div>

  <div class="blocklist--striped" style="--primary-color: rgba(0, 0, 0, .04); --secondary-color: transparent;">
    <div>This is a stripped block list.</div>
    <div>It's responsive.</div>
    <div>Color can be customized by --primary-color and --secondary-color.</div>
  </div>
        
</div>

        """)%}</code></pre>

        '''
    }
  },

  {
    'file': 'docs/list.html',
    'template': template_raw,
    'vars': {
        'doc': r'''
        <h3>List</h3>

        <div style="display: flex; margin-bottom: 0;">

          <div class="list" style="margin: 0 2em 2em 0;">
            <button class="list-button">Item 1</button>
            <button class="list-button">Item 2</button>
            <button class="list-button">Item 3</button>
          </div>

          <div class="list" style="color: rgba(160, 0, 0, .8); margin: 0 2em 2em 0;">
            <button class="list-button">Customize color</button>
            <button class="list-button">By setting style</button>
            <button class="list-button">Of the list div</button>
          </div>

        </div>

        <pre><code>{%
          syntax_highlight("""

<div class="list">
  <button class="list-button">Item 1</button>
  <button class="list-button">Item 2</button>
  <button class="list-button">Item 3</button>
</div>

<div class="list" style="color: rgba(160, 0, 0, .8);">
  <button class="list-button">Customize color</button>
  <button class="list-button">By setting style</button>
  <button class="list-button">Of the list div</button>
</div>
       """)%}</code></pre>


        <h3>Collapse List</h3>

        <div style="display: flex;">
          <div class="list" style="height: 13em; border: 1px solid rgba(0, 0, 0, .12);">
            <div class="list-item--expand" onclick="LM.collapse_list_set_top(this);"><button class="collapse-list-button">Item 1, click to top me!</button></div>
            <div class="list-item--expand" onclick="LM.collapse_list_set_top(this);"><button class="collapse-list-button">Item 2, click to top me!</button></div>
            <div class="list-item--expand" onclick="LM.collapse_list_set_top(this);"><button class="collapse-list-button">Item 3, click to top me!</button></div>
          </div>
        </div>


        <pre><code>{%
          syntax_highlight("""

<div class="list" style="height: 13em; border: 1px solid rgba(0, 0, 0, .12);">
  <div class="list-item--expand" onclick="LM.collapse_list_set_top(this);">
    <button class="collapse-list-button">Item 1, click to top me!</button>
  </div>
  <div class="list-item--expand" onclick="LM.collapse_list_set_top(this);">
    <button class="collapse-list-button">Item 2, click to top me!</button>
  </div>
  <div class="list-item--expand" onclick="LM.collapse_list_set_top(this);">
    <button class="collapse-list-button">Item 3, click to top me!</button>
  </div>
</div>

       """)%}</code></pre>
        '''
    }
  },

  {
    'file': 'docs/table.html',
    'template': template_raw,
    'vars': {
        'doc': r'''
        <h3>Table</h3>

        <div style="display: flex; margin-bottom: 2em;">
          <div class="table">
            <table>
              <thead>
                <tr>
                  <th>Name</td>
                  <th>Age</td>
                  <th>Email</td>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Foo</td>
                  <td>13</td>
                  <td>foo@gmail.com</td>
                </tr>
                <tr>
                  <td>Bar</td>
                  <td>14</td>
                  <td>bar@outlook.com</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <pre><code>{%
          syntax_highlight("""
<div class="table">
  <table>

    <thead>
      <tr>
        <th>Name</td>
        <th>Age</td>
        <th>Email</td>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td>Foo</td>
        <td>13</td>
        <td>foo@gmail.com</td>
      </tr>
      <tr>
        <td>Bar</td>
        <td>14</td>
        <td>bar@outlook.com</td>
      </tr>
    </tbody>

  </table>
</div>
       """)%}</code></pre>

        <h3>Striped Table</h3>

        <div style="display: flex; margin-bottom: 2em;">
          <div class="table--striped">
            <table>
              <thead>
                <tr>
                  <th>Model</td>
                  <th>Performance</td>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>MASS</td>
                  <td onclick="LM.modify(this, '123')" style="cursor: pointer;">42.1</td>
                </tr>
                <tr>
                  <td>BART</td>
                  <td>44.2</td>
                </tr>
                <tr>
                  <td>T5</td>
                  <td>43.5</td>
                </tr>
                <tr>
                  <td>PEGASUS</td>
                  <td>43.9</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <pre><code>{%
          syntax_highlight("""
<div class="table--striped">
  <table>
    <thead>
      <tr>
        <th>Model</td>
        <th>Performance</td>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>MASS</td>
        <td onclick="LM.modify(this, '123')" style="cursor: pointer;">42.1</td>
      </tr>
      <tr>
        <td>BART</td>
        <td>44.2</td>
      </tr>
      <tr>
        <td>T5</td>
        <td>43.5</td>
      </tr>
      <tr>
        <td>PEGASUS</td>
        <td>43.9</td>
      </tr>
    </tbody>
  </table>
</div>
 
       """)%}</code></pre>

        <div class="note"><p><strong>NOTE</strong></p>
          <p>We use LM.modify function to modify content of cells dynamically.</p>
        </div>

        '''
    }
  },

  {
    'file': 'docs/hmf.html',
    'template': template_raw,
    'vars': {
        'doc': r'''

        <h3>Header Main Footer</h3>

        <p>As a variance of <strong>Holy Grail</strong> layout, HMF consists of header, main content(nav and content) and footer. </p>

        <div>

<div class="hmf--dense" style="min-height: 10em;">

  <header>
    <div>
      <button class="icon"><i class="material-icons">menu</i></button>
      <span class="middle">HMF</span>
      <a class="right-start">About</a>
      <a>More</a>
    </div>
  </header>

  <main>

    <nav class="nav-menu">
      <ul>
        <li><a>Getting Started</a></li>
        <li class="section" style="--lines: 3;">
          <input type="checkbox" id="cb1">
          <label for="cb1">Variances</label>
          <ul>
            <div>
              <li><a>Landscape</a></li>
              <li><a>Portrait</a></li>
              <li><a>Responsive</a></li>
            </div>
          </ul>
        </li>
      </ul>
    </nav>

    <div class="mark">

      <h3>Hello</h3>
      <p>This is a demo of responsive <a href="">HMF</a>.</p>
      <p>You can scale to see different states.</p>

    </div>
  </main>

  <footer>
    footer
  </footer>

</div>

        </div>


        <pre><code>{%
          syntax_highlight("""

<body class="hmf--dense">

  <header>
    <div>
      <button class="icon"><i class="material-icons">menu</i></button>
      <span class="middle">HMF</span>
      <a class="right-start">About</a>
      <a>More</a>
    </div>
  </header>

  <main>

    <nav class="nav-menu">
      <ul>
        <!-- Normal Item -->
        <li><a>Getting Started</a></li>
        <!-- Collapse Item: set "lines" to the number of subitems -->
        <li class="section" style="--lines: 3;">
          <input type="checkbox" id="cb1">
          <label for="cb1">Variances</label>
          <ul>
            <div>
              <li><a>Landscape</a></li>
              <li><a>Portrait</a></li>
              <li><a>Responsive</a></li>
            </div>
          </ul>
        </li>
      </ul>
    </nav>

    <div class="mark">

      <h3>Hello</h3>
      <p>This is a demo of responsive <a href="">HMF</a>.</p>
      <p>You can scale to see different states.</p>

    </div>
  </main>

  <footer>
    footer
  </footer>

</div>


       """)%}</code></pre>


        <h3>Header</h3>

        <p>Alignment of items is controlled by <code><span class="value">middle</span></code> and <code><span class="value">right-start</span></code>, i.e., label the middle item by <code><span class="value">middle</span></code> and the left-most item in the right region by <code><span class="value">right-start</span></code>.</p>

        <p>Sticky header can be achieved by styling as follows.</p>

        <pre><code>{%
          syntax_highlight("""
<header style="position: sticky; top: 0; z-index: 10;">
    ...
</header>
       """)%}</code></pre>



        <h3>Navigation</h3>

        <p>Both collapse and non-collapse items are allowed. Remember to set <code><span class="value">--lines</span></code> to the number of subitems to collapse.

        <h3>Main Content</h3>

        <p>Utilize <code><span class="value">mark</span></code> for styling font size and spacing. 

          <code>&lt;<span class="title">h1</span>&gt;</code>,
          <code>&lt;<span class="title">h2</span>&gt;</code>, 
          <code>&lt;<span class="title">h3</span>&gt;</code>,
          <code>&lt;<span class="title">p</span>&gt;</code>,
          <code>&lt;<span class="title">a</span>&gt;</code>,
          <code>&lt;<span class="title">img</span>&gt;</code>

          are highly recommended.

        </p>

        <h3>Footer</h3>

        <p>A <strong>stick footer</strong>, or a <strong>bottom bar</strong>, can also be achieved by styling the footer as follows.</p>

        <pre><code>{%
          syntax_highlight("""
<footer style="position: sticky; bottom: 0; z-index: 10;">
    ...
</footer>
       """)%}</code></pre>

        <div class="note"><p><strong>NOTE</strong></p>
          <p>If you don't need the footer, just delete it.</p>
        </div>

       
        '''
    }
  
  },  

]

def generate_nav(generate_cnt=0):
    
    # Only need to modify this for routing
    nav = [
        # Single level
        ["", "Getting Started"], 

        # Two level
        ["Components", 
            "Button",
            "Toggle Button", 
            "Input", 
            "Select", 
            "Rating", 
            "SVG", 
            "Card", 
            "Toast", 
        ],

        ["Containers", 
            "Mark", 
            "List", 
            "Table",
        ],

        ["Views", 
            "HMF",
        ],

        ["Demos", 
            "Chat",
            "Forum",
            "Profile",
            "Timetable",
        ],
    ]

    html = "<ul>"

    for i, item in enumerate(nav):

        tmp = ""
        for x in item[1:]:
            url = "-".join(x.strip().lower().split()).strip() + ".html";
            if item[0] == "Demos":
                tmp += f"<li><a href='{url}'>{x}</a></li>"
            else:
                tmp += f"""
                    <li><a href="#{url}">{x}</a></li>
                """

        html += (f"""
            <li class="section" style="--lines: {len(item) - 1};">
              <input type="checkbox" id="{generate_cnt}cm{i}">
              <label for="{generate_cnt}cm{i}">{item[0]}</label>
              <ul>
                <div>
            """ + tmp + "</div></ul></li>") if item[0] else tmp

    generate_cnt += 1
    return html + "</ul>" 

def syntax_highlight(s):

    s = s.strip()
    rtn = ''

    in_tag = False
    in_comment = False
    tag_content = ''

    i = 0
    l = len(s)
    while i < l:

        c = s[i]

        if c == '<':

            if i+3 < l and s[i: i+4] == '<!--':
                in_comment = True
                rtn += '<span class="comment">&lt;'

            else: 
                in_tag = True
                rtn += '<span class="tag">&lt;'

            # Eat not-a-word characters
            if s[i+1] == '/':
                i += 1
                rtn += s[i]
            
        elif c == '>':

            if in_comment and i-2 >= 0 and s[i-2: i+1] == "-->":
                in_comment = False
                rtn += tag_content

            else:

                in_tag = False

                tag_content = tag_content.strip()

                in_title = True
                in_attr = False
                in_value = False
                value_cnt = 0

                rtn += '<span class="title">'

                tl = len(tag_content)
                for j, c in enumerate(tag_content.strip()):

                    rtn += c
                    if in_title:

                        if j+1 >= tl or tag_content[j+1] == ' ': 
                            in_title = False
                            rtn += '</span>'

                    elif in_attr:

                        if j+1 >= tl or tag_content[j+1] == '=' or tag_content[j+1] == ' ':
                            in_attr = False
                            rtn += '</span>'
                    
                    elif in_value:

                        if c == '"':
                            value_cnt += 1
                            if value_cnt == 2:
                                in_value = False
                                rtn += '</span>'
                                value_cnt = 0

                    else:
                        # only support ""
                        if j+1 < tl and tag_content[j+1] == '"':
                            rtn += '<span class="value">'
                            in_value = True

                        elif j+1 < tl and tag_content[j+1] != '"' and tag_content[j+1] != ' ':
                            rtn += '<span class="attr">'
                            in_attr = True
                    

            rtn += '&gt;</span>'
            tag_content = ''

        elif in_tag:
            tag_content += c

        else:
            rtn += c
        
        i += 1
    
    return rtn




for src in srcs:

    output_file = ''

    if 'template' not in src:
        print(src)

    output_src = src['template']
   

    # Templating
    for key, value in src.items():

        if key == 'file': 
            output_file = value

        elif key == 'vars':
            for var, val in value.items():
                output_src = re.sub('{%' + f'{var}' + '%}', val, output_src)
   
    assert output_file != ''
    # assert output_src != template

    # Parsing
    while True:
        match = re.search(r'\{%\s*((?:[^%]|%(?!}))*)\s*%\}', output_src, re.DOTALL)

        if match is None:
            break

        si, ei = match.start(), match.end()
        code = match.group(1)

        insert = ''
        # code or value
        try: 
            insert = eval(code.strip())
        except:
            exec(code)
            insert = ''
        
        output_src = output_src[:si] + insert + output_src[ei:]

    with open(output_file, 'w') as f:
        f.write(output_src)

