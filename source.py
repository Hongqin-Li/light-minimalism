# Generate Documents

import re
import os

os.system('sass light-minimalism.scss docs/light-minimalism.css')
os.system('cp light-minimalism.js docs/light-minimalism.js')

template = '''

<html>
  <head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>

    <link rel="stylesheet" href="light-minimalism.css"/>

    <!-- Icon -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css" rel="stylesheet">

  </head>

<body class="hmf--dense">

  <header>
    <div>
      <span>LIGHT-MINIMALISM</span>
      <a class="right-start" href="https://github.com/Xinhong-Li/light-minimalism">Github</a>
    </div>
  </header>

  <main>

    <!--left menu(optional)-->
    <nav class="nav-menu">
      <ul>

      <li><a href="started.html">Getting Started</a></li>

      <li class="section" style="--lines: 6;">
        <input type="checkbox" id="cm1">
        <label for="cm1">Components</label>
        <ul>
          <div>
            <li><a href="button.html">Button</a></li>
            <li><a href="toggle-button.html">Toggle Button</a></li>
            <li><a href="input.html">Input</a></li>
            <li><a href="card.html">Card</a></li>
            <li><a href="dialog.html">Dialog</a></li>
            <li><a href="toast.html">Toast</a></li>
          </div>
        </ul>
      </li>

      <li class="section" style="--lines: 2;">
        <input type="checkbox" id="cm2">
        <label for="cm2">Containers</label>
        <ul>
          <div>
            <li><a href="mark.html">Mark</a></li>
            <li><a href="list.html">List</a></li>
          </div>
        </ul>
      </li>


      <li class="section" style="--lines: 1;">
        <input type="checkbox" id="cm3">
        <label for="cm3">Views</label>
        <ul>
          <div>
            <li><a href="hmf.html">HMF</a></li>
          </div>
        </ul>
      </li>

      <li><a href="testing.html">Testing</a></li>


      </ul>
    </nav>

    <div class="mark reveal">
      {%doc%}
    </div>

  </main>

  <!--
  <footer>
    <div class="inputbar">
    <button class="contained">SEND</button>
    </div>
  </footer>
  -->

</body>
<script type="text/javascript" src="light-minimalism.js"></script>

</html>

'''


srcs = [
  {
    'file': 'docs/index.html',
    'template': template,
    'vars': {
        'doc': 'index'
    }
  },

  {
    'file': 'docs/started.html',
    'template': template,
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
    'template': template,
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
    'template': template,
    'vars': {
        'doc': '''

        <h3>Toggle Button</h3>

        <p>A toggle button is a button that represents a setting with two states, such as <code><span class="value">switch</span></code>, <code><span class="value">checkbox</span></code> and <code><span class="value">radio button</span></code>.</p>

        <div style="display: flex; flex-wrap: wrap; align-items: flex-end; margin-bottom: 0;">
          <span class="switch" style="margin: 0 2em 2em 0;">
            <input type="checkbox"><span></span>
          </span>
          <span class="checkbox" style="margin: 0 2em 2em 0;">
            <input type="checkbox"><span></span>
          </span>
          <span class="radio" style="margin: 0 2em 2em 0;">
            <input type="radio"><span></span>
          </span>
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
    'template': template,
    'vars': {
        'doc': '''
        <h3>Input</h3>
        
        <div style="display: flex; flex-wrap: wrap; align-items: flex-start; margin-bottom: 0;">

          <span class="input--outlined" style="margin: 0 2em 2em 0;">
            <input type="text" placeholder="This is an outlined input..."/><span></span>
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

        </div>

        <pre><code>{%
          syntax_highlight("""
<span class="input--outlined">
  <input type="text" placeholder="This is an outlined input..."/><span></span>
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

        """)%}</code></pre>

         
        <h3>Input Bar</h3>

        <p>This can be a search bar.</p>

        <div>
          <div class="inputbar" style="width: 100%;">
            <input type="text" placeholder="Please input sth...">
            <span style="--width: 5em;"><span>Send</span></span>
          </div>
        </div>

        <pre><code>{%
          syntax_highlight("""
<div class="inputbar" style="width: 100%;">
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
    'template': template,
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

  { 'file': 'docs/toast.html',
    'template': template,
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
    'template': template,
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
    'file': 'docs/mark.html',
    'template': template,
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

</div>

        """)%}</code></pre>

        '''
    }
  },

  {
    'file': 'docs/list.html',
    'template': template,
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

        <div>
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
    'file': 'docs/hmf.html',
    'template': template,
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

  {
    'file': 'docs/testing.html',
    'template': '''
<!DOCTYPE html>
  <head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>

    <link rel="stylesheet" href="light-minimalism.css"/>

    <!-- Icon -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css" rel="stylesheet">

  </head>

<body class="hmf--dense">

  <div class="toast--hide">
    <div>
        This is a toast.
    </div>
  </div>

  <!-- signin dialog -->
  <input class="dialog-trigger" id="signin-dialog-trigger" type="checkbox" checked/>
  <div class="dialog-container frosted-glass" style="z-index: 12; background-color: white;">

    <div class="dialog-content">

      <div class="mark">
        <h3>Please sign in.</h3>

        <div class="inputbar" style="max-width: 20em;">
            <input id="signinname" type="text">
            <span style="--width: 5em;"><span>Name</span></span>
        </div>

        <div class="inputbar" style="max-width: 20em;">
            <input id="signinpwd" type="text">
            <span style="--width: 7em;"><span>Password</span></span>
        </div>

        <div>
          <button id="signinbtn" class="light" style="color: rgba(0, 0, 0, .8);">Sign In</button>
        </div>


        <p>Do not have an account? <a><label for="signup-dialog-trigger" style="cursor:pointer;">Create one now.</label></a></p>

        <!-- Action buttons -->
        <div style="text-align: right;">
          <label for="signin-dialog-trigger" style="align-self: flex-end;"><a class="icon"><i class="material-icons">navigate_before</i></a></label>
        </div>
      </div>

    </div>

  </div>

  <!-- signup dialog -->
  <input class="dialog-trigger" id="signup-dialog-trigger" type="checkbox"/>
  <div class="dialog-container frosted-glass" style="z-index: 12; background-color: white;">

    <div class="dialog-content">

      <div class="mark">
        <h3>Welcome.</h3>

        <div class="inputbar" style="max-width: 20em;">
            <input id="signupname" type="text">
            <span style="--width: 5em;"><span>Name</span></span>
        </div>

        <div class="inputbar" style="max-width: 20em;">
            <input id="signuppwd" type="text">
            <span style="--width: 7em;"><span>Password</span></span>
        </div>

        <div>
          <button id="signupbtn" class="light" style="color: rgba(0, 0, 0, .8);">Sign Up</button>
        </div>

        <!-- Action buttons -->
        <div style="text-align: right;">
          <label for="signup-dialog-trigger" style="align-self: flex-end;"><a class="icon"><i class="material-icons">navigate_before</i></a></label>
        </div>
      </div>

    </div>

  </div>

  <!-- add chat dialog -->
  <input class="dialog-trigger" id="addchat-dialog-trigger" type="checkbox"/>
  <div class="dialog-container frosted-glass" style="z-index: 12; background-color: white;">

    <div class="dialog-content">

      <div class="mark">

        <h3>Join a new chat.</h3>

        <p>Join a chat with a secret key. Everyone with the same key will be added to this chat.</p>

        <div class="inputbar" style="max-width: 20em;">
            <input id="joinchatinput" type="text">
            <span style="--width: 5em;"><span>Any</span></span>
        </div>

        <div>
          <button id="joinchatbtn" class="light" style="color: rgba(0, 0, 0, .8);">Join</button>
        </div>

        <!-- Action buttons -->
        <div style="text-align: right;">
          <label for="addchat-dialog-trigger" style="align-self: flex-end;"><a class="icon"><i class="material-icons">navigate_before</i></a></label>
        </div>
      </div>

    </div>

  </div>



  <header class="landscape-only">
    <div style="height: 3em; align-items: center;">
      <span>Mr. Foolbar</span>

      <label for="signin-dialog-trigger" class="right-start" style="display: flex; align-items: center;">
        <a class="icon"><i class="material-icons">account_circle</i></a>
      </label>

    </div>
  </header>

  <input type="checkbox" id="menu-trigger" class="hmf--fullscreen-trigger"/>
  <header class="portrait-sticky frosted-glass portrait-only" style="top: 0; z-index: 11;">

    <!-- header row 1 -->
    <div style="height: 3em; align-items: center;">
      <span>Mr. Foolbar</span>
      <label for="signin-dialog-trigger" class="right-start" style="display: flex; align-items: center;">
        <a class="icon"><i class="material-icons">menu</i></a>
      </label>
    </div>

    <!-- header row 2(dropdown box) -->
    <div style="height: calc(100vh - 3rem); display: block; overflow-y: auto; padding-top: 0;">

    <nav class="nav-menu" style="width: 100%;">
      <ul id="portraitchatlist">

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
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>
        <li><a>Getting Started</a></li>

      </ul>
    </nav>

    </div>

  </header>

  <main style="padding-top: 0; padding-bottom: 0; justify-content: flex-start;">

    <!--left menu -->
    <nav class="nav-menu landscape-only noscrollbar--outer" 
         style="position: sticky;
                top: 0;
                height: calc(100vh - 3rem);
                width: 15rem;
                border: 1px solid rgba(0, 0, 0, .12); border-top: none; border-bottom: none;">

        <div class="noscrollbar--inner">

            <div id="landscapechatlist" class="noscrollbar--content list" style="height: calc(100vh - 3rem); width: 15rem;">
              <div style="width: 100%; padding: 1em; display: flex;
                border: 1px solid rgba(0, 0, 0, .12);
                border-left: none; border-right: none;
                border-top: none;
              ">
                <span class="input--light">
                  <input type="text" placeholder="Search..." style="display: inline-block;"><span></span>
                  <i class="material-icons" style="cursor: pointer;"><label for="addchat-dialog-trigger" style="padding: 0; color: currentColor; background: none;">add</label></i>
                </span>
              </div>

                <!--button class="list-button">d</button-->
     
            </div>
        </div>
    </nav>

    <div class="mark" style="max-width: 50rem; overflow: hidden;">

        <div id="dialog" style="display: flex; flex-direction: column; align-items: flex-start; margin-top: 1.5em;">

            <div class="card--outlined"
                 style="align-self: center;
                        color: rgba(0, 0, 0, .6);
                        background-color: rgba(0, 0, 0, .04);
                        margin-bottom: 1em;
                 ">Today at 19: 13</div>

            <div class="card--outlined" 
                 style="border-radius: 1em 1em 0 1em;
                        align-self: flex-end;
                        margin-bottom: 1em;">
              Hey, man! what's up?</div>

            <div class="card--flat" style="
                border-radius: 1em 1em 1em 0em;
                background-color: rgba(0, 0, 0, .8);
                color: white;
                align-self: flex-start;
                margin-bottom: 1em;
            ">Hello guy! Have you finished your PJ?
            </div>

            <div class="card--outlined" style="border-radius: 1em 1em 0 1em; align-self: flex-end; margin-bottom: 1em;">
              What?</div>
            <div class="card--outlined" style="border-radius: 1em 1em 0 1em; align-self: flex-end; margin-bottom: 1em;">
              PJ?</div>
            <div class="card--outlined" style="border-radius: 1em 1em 0 1em; align-self: flex-end; margin-bottom: 1em;">
              I haven't even known about it...</div>
            <div class="card--outlined" style="border-radius: 1em 1em 0 1em; align-self: flex-end; margin-bottom: 1em;">
              ...</div>
            <div class="card--outlined" style="border-radius: 1em 1em 0 1em; align-self: flex-end; margin-bottom: 1em;">
              ...</div>
            <div class="card--outlined" style="border-radius: 1em 1em 0 1em; align-self: flex-end; margin-bottom: 1em;">
              ...</div>
            <div class="card--outlined" style="border-radius: 1em 1em 0 1em; align-self: flex-end; margin-bottom: 1em;">
              ...</div>
        </div>

    </div>

  </main>

  <footer class="sticky-bar" style="height: 3em">
    <div class="middle inputbar" style="max-width: 40em; padding:0; align-items: center; border: none;">
        <input type="text" id="sendinput" placeholder="Please input sth...">
        <span id="sendbtn" style="--width: 5em;"><span>Send</span></span>
    </div>
  </footer>

</body>
<script type="text/javascript" src="light-minimalism.js"></script>
<script type="text/javascript" src="chat.js"></script>

</html>
    ''',
  },


]

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

