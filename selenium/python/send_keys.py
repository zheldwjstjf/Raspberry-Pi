"""
[ 1. Example ]
"""

from selenium.webdriver.common.keys import Keys

element.send_keys(Keys.ENTER)
element.send_keys(Keys.ARROW_LEFT)
element.send_keys(Keys.BACK_SPACE)



"""
[ 2. send_keys ]

Help on module selenium.webdriver.remote.webelement in selenium.webdriver.remote:

NAME
    selenium.webdriver.remote.webelement

DESCRIPTION
    # Licensed to the Software Freedom Conservancy (SFC) under one
    # or more contributor license agreements.  See the NOTICE file
    # distributed with this work for additional information
    # regarding copyright ownership.  The SFC licenses this file
    # to you under the Apache License, Version 2.0 (the
    # "License"); you may not use this file except in compliance
    # with the License.  You may obtain a copy of the License at
    #
    #   http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing,
    # software distributed under the License is distributed on an
    # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    # KIND, either express or implied.  See the License for the
    # specific language governing permissions and limitations
    # under the License.

CLASSES
    builtins.object
        WebElement
    
    class WebElement(builtins.object)
     |  WebElement(parent, id_, w3c=False)
     |  
     |  Represents a DOM element.
     |  
     |  Generally, all interesting operations that interact with a document will be
     |  performed through this interface.
     |  
     |  All method calls will do a freshness check to ensure that the element
     |  reference is still valid.  This essentially determines whether or not the
     |  element is still attached to the DOM.  If this test fails, then an
     |  ``StaleElementReferenceException`` is thrown, and all future calls to this
     |  instance will fail.
     |  
     |  Methods defined here:
     |  
     |  __eq__(self, element)
     |      Return self==value.
     |  
     |  __hash__(self)
     |      Return hash(self).
     |  
     |  __init__(self, parent, id_, w3c=False)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __ne__(self, element)
     |      Return self!=value.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |

     ...
        
     |  send_keys(self, *value)
     |      Simulates typing into the element.
     |      
     |      :Args:
     |          - value - A string for typing, or setting form fields.  For setting
     |            file inputs, this could be a local file path.
     |      
     |      Use this to send simple key events or to fill out form fields::
     |      
     |          form_textfield = driver.find_element_by_name('username')
     |          form_textfield.send_keys("admin")
     |      
     |      This can also be used to set file inputs.
     |      
     |      ::
     |      
     |          file_input = driver.find_element_by_name('profilePic')
     |          file_input.send_keys("path/to/profilepic.gif")
     |          # Generally it's better to wrap the file path in one of the methods
     |          # in os.path to return the actual path to support cross OS testing.
     |          # file_input.send_keys(os.path.abspath("path/to/profilepic.gif"))

     ...
        




[ 3. Keys ]

(base) jack (master) python
$ python
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import selenium.webdriver.common.keys
>>> help(selenium.webdriver.common.keys)

Help on module selenium.webdriver.common.keys in selenium.webdriver.common:

NAME
    selenium.webdriver.common.keys - The Keys implementation.

CLASSES
    builtins.object
        Keys
    
    class Keys(builtins.object)
     |  Set of special keys codes.
     |  
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  ADD = '\ue025'
     |  
     |  ALT = '\ue00a'
     |  
     |  ARROW_DOWN = '\ue015'
     |  
     |  ARROW_LEFT = '\ue012'
     |  
     |  ARROW_RIGHT = '\ue014'
     |  
     |  ARROW_UP = '\ue013'
     |  
     |  BACKSPACE = '\ue003'
     |  
     |  BACK_SPACE = '\ue003'
     |  
     |  CANCEL = '\ue001'
     |  
     |  CLEAR = '\ue005'
     |  
     |  COMMAND = '\ue03d'
     |  
     |  CONTROL = '\ue009'
     |  
     |  DECIMAL = '\ue028'
     |  
     |  DELETE = '\ue017'
     |  
     |  DIVIDE = '\ue029'
     |  
     |  DOWN = '\ue015'
     |  
     |  END = '\ue010'
     |  
     |  ENTER = '\ue007'
     |  
     |  EQUALS = '\ue019'
     |  
     |  ESCAPE = '\ue00c'
     |  
     |  F1 = '\ue031'
     |  
     |  F10 = '\ue03a'
     |  
     |  F11 = '\ue03b'
     |  
     |  F12 = '\ue03c'
     |  
     |  F2 = '\ue032'
     |  
     |  F3 = '\ue033'
     |  
     |  F4 = '\ue034'
     |  
     |  F5 = '\ue035'
     |  
     |  F6 = '\ue036'
     |  
     |  F7 = '\ue037'
     |  
     |  F8 = '\ue038'
     |  
     |  F9 = '\ue039'
     |  
     |  HELP = '\ue002'
     |  
     |  HOME = '\ue011'
     |  
     |  INSERT = '\ue016'
     |  
     |  LEFT = '\ue012'
     |  
     |  LEFT_ALT = '\ue00a'
     |  
     |  LEFT_CONTROL = '\ue009'
     |  
     |  LEFT_SHIFT = '\ue008'
     |  
     |  META = '\ue03d'
     |  
     |  MULTIPLY = '\ue024'
     |  
     |  NULL = '\ue000'
     |  
     |  NUMPAD0 = '\ue01a'
     |  
     |  NUMPAD1 = '\ue01b'
     |  
     |  NUMPAD2 = '\ue01c'
     |  
     |  NUMPAD3 = '\ue01d'
     |  
     |  NUMPAD4 = '\ue01e'
     |  
     |  NUMPAD5 = '\ue01f'
     |  
     |  NUMPAD6 = '\ue020'
     |  
     |  NUMPAD7 = '\ue021'
     |  
     |  NUMPAD8 = '\ue022'
     |  
     |  NUMPAD9 = '\ue023'
     |  
     |  PAGE_DOWN = '\ue00f'
     |  
     |  PAGE_UP = '\ue00e'
     |  
     |  PAUSE = '\ue00b'
     |  
     |  RETURN = '\ue006'
     |  
     |  RIGHT = '\ue014'
     |  
     |  SEMICOLON = '\ue018'
     |  
     |  SEPARATOR = '\ue026'
     |  
     |  SHIFT = '\ue008'
     |  
     |  SPACE = '\ue00d'
     |  
     |  SUBTRACT = '\ue027'
     |  
     |  TAB = '\ue004'
     |  
     |  UP = '\ue013'

DATA
    unicode_literals = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', ...

FILE
    /anaconda3/lib/python3.7/site-packages/selenium/webdriver/common/keys.py

"""
