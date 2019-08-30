# Generate Documents

import re
import os

os.system('scss light-minimalism.scss docs/light-minimalism.css')


template = '''

<html>
  <head>
    <meta charset="utf-8"/>
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

      <li class="section" style="--lines: 2;">
        <input type="checkbox" id="cm1">
        <label for="cm1">Components</label>
        <ul>
          <div>
            <li><a href="button.html">Button</a></li>
            <li><a href="toggle-button.html">Toggle Button</a></li>
          </div>
        </ul>
      </li>

      <li class="section" style="--lines: 1;">
        <input type="checkbox" id="cm2">
        <label for="cm2">Containers</label>
        <ul>
          <div>
            <li><a href="mark.html">Mark</a></li>
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


      </ul>
    </nav>

    <div class="mark reveal">
      {%doc%}
    </div>

  </main>

  <!--
  <footer>
    <div>footer</div>
  </footer>
  -->

</body>

</html>

'''


srcs = [
  {
    'file': 'docs/index.html',
    'vars': {
        'doc': 'index'
    }
  },

  {
    'file': 'docs/started.html',
    'vars': {
        'doc': r'''

        <h3>Getting Started</h3>

        <p>Download css and js file and then include them in html as the boilderplate shown below.</p>

        <pre><code>{%
          syntax_highlight("""

<html>
  <head>
    <meta charset="utf-8"/>

    <!-- CSS -->
    <link rel="stylesheet" href="light-minimalism.css"/>

    <!-- Optional: Icon -->
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css" rel="stylesheet">

    <!-- Optional: Font -->
    <link href="https://fonts.font.im/css?family=Montserrat" rel="stylesheet">

  </head>

  <body>
    <!-- Contents here -->
  </body>

</html>


          """)%}</code></pre>

        '''
    }
  },

  {
    'file': 'docs/button.html',
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

  {
    'file': 'docs/mark.html',
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
    'file': 'docs/hmf.html',
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
        <!-- Collapse Item: set --lines to the number of subitems -->
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

       
        '''
    }
  
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
    output_src = template

    # Templating
    for key, value in src.items():

        if key == 'file': 
            output_file = value

        elif key == 'vars':
            for var, val in value.items():
                output_src = re.sub('{%' + f'{var}' + '%}', val, output_src)
   
    assert output_file != ''
    assert output_src != template

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

