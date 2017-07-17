 
Logictools overview
======================================

Introduction
--------------------

The *logictools* overlay enables a Python programmer to create programmable logic circuits that interface to, and control, input-output (IO) signals.  Using the *logictools* library, the programmer can specify, in Python, the digital IO pins he would like to control, and the functions and/or logic values he wants to apply to them.  The API is declarative so the programmer only needs to specify what he wants and the libray will transform his specifications into the necessary circuits. *logictools* also allows the Python programmer to record and observe the operation of the circuits.  


*logictools* overlay operation
-----------------------------------------

We will look first at a block diagram of the *logictools* overlay.  Once we understand how it works, we will learn how to program it, using the functions in the *logictools* API.

Logictools overlay block diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../../images/logictools_bd.png
   :height: 100px
   :width: 200px
   :scale: 75%
   :align: center

From the block diagram, we can see five highlighted blocks in the programmable logic (PL) section of the Zynq device.  These are the:

* Boolean Generator
* Pattern Generator
* FSM Generator
* Trace Analyzer, and
* Interface Switch

The functions each block performs are specified by Python scripts running on the ARM A9's in the processor subsystem (PS).  The logictools overlay also contains a MicroBlaze subsystem which controls all the other blocks, as directed by the ARM A9s.  Three of the five blocks are *generator* blocks.  This means that we can use each of them to *generate* digital signals.  Let's review each of the three generators, in turn.  After that, we will review the Interface Switch and the Trace Analyzer.   

**Boolean Generator**

The Boolean Generator is an input-output block.  We use the Boolean Generator to generate combinational, Boolean functions which we apply to the inputs of the functions in the Boolean Generator.  The function output appears on a corresponding output pin.  The Boolean Generator can generate multiple, independent, combinatonal Boolean functions simulaneously.  The functions and the pins to which they are applied are specified in Python using the *logictools* API.

**Pattern Generator**

The Pattern Generator is an output block.  With this block, we can specify a sequence of logic values which we want to appear on its output pins.  These sequences of logic values are known as *digital patterns*.  A digital pattern can be applied to multiple pins simultaneously.  The values on each pin are completely independent of the values on any other pin.  Each value is applied to a pin, for one or more clock cycles, as determined by the pattern specification. The patterns and the pins to which they are applied are specified in Python using the *logictools* API.

**FSM Generator**

The Boolean Generator is an input-output block.  The acronym *FSM* is short for *Finite State Machine* (sometimes referred to as an automaton).  FSMs allow us to construct *stateful* Boolean machines.  A simple example of a FSM is a binary counter, which increments its value every time it is stimulated by a clock signal.   The key characteristic of FSMs is that they incorporate memory elements so they are capable or remembering what state they are in, at any time.  With the FSM Generator, we specify in Python which pins we want as the inputs to the FSM, and which pins we want as its outputs.  We can then completely specify the behavior of our FSM, and the FSM Generator will realize the FSM circuit for that behavior.

Note that both the Pattern Generator and FSM Generator are connected to a direct memory access (DMA) unit which is controlled by the MicroBlaze subsystem, as directed by the Python scripts running on the ARM A9 CPUs. The DMA is used to stream configuration data to the Pattern Generator and FSM.

**Interface Switch**

The Interface Switch is a programmable switch that connects to external IO pins of the PL.  Each of the generators is also connected to the Interface Switch.  By programming the switch, from the *logictools* API, we can decide which pins are inputs and which pins are outputs for our design.  We also declare which generator pins should connect to each of these IO signals.  The programmability of the Interface Switch allows us to use the *logictools* overlay to interface to lots of different external devices.  We simply have to change the pin definitions to match the pin-outs of whatever external device we are connecting to. 

When combined with one or more of the generators, the Interface Switch enables us to interface to, and interact with, a wide variety of digital devices and circuits. 

**Trace Analyzer**

The Trace Analyzer is an input-only block.  Unlike the generators, it is connected to the output of the Interface Switch.  All of the IO signals appear as inputs to the Trace Analyzer.  These signals may be outputs driven by the generators, or inputs to the PL that are driven by external circuits.  The Trace Analyzer captures and records the IO signals. Its output is connected to a DMA unit which streams the data back to the DRAM in the PS to be post-processed by Python scripts running on the ARM A9 CPUs in the PS.  The Trace Analyzer allows us to verify that the output signals we have specified from the generators are being applied correctly.  It also allows us to debug and analyze the opearion of the external interface.  

The PYNQ-Z1 logictools overlay
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The block diagram for the PYNQ-Z1 logictools overlay is shown below.

.. image:: ../../images/PYNQ-Z1_logictools_bd.png
   :height: 100px
   :width: 200px
   :scale: 75%
   :align: center


The most significant change from the earlier, more generic block diagram of the logictools overlay is that the IO interface is specified in more detail.  For the PYNQ-Z1 board, this interface is the Arduino shield interface, or more precisely those pins of the Arduino shield interface that can be configured as general-purpose IO pins.  The GPIO pin set includes pins D0-D13 and A0-A5 inclusive.  Any Arduino pin may be configured as input or output and may be connected to any Generator pin so long as the pin is not already in use elsewhere.

In adddition to the 20 Ardunio GPIO pins, the 4 pushbuttons and 4 green LEDs of the PYNQ-Z1 board are also included.  The pushbuttons and LEDs are special, because they can only be connected to the inputs and outputs of the Boolean Generator, respectively.

The block diagram of the PYNQ-Z1 logictools overlay also shows the block RAMs (BRAM) used in the Pattern Generator, FSM Generator and the Trace Analyzer. The size of each BRAM is shown in kilo bytes.



Logictools IP and  project files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The source code for all the hardware blocks is provided. Each block can also be reused as a standalone IP in a custom overlay. 

The source files for the logictools IP can be found in the same location as the other PYNQ IP:

.. code-block:: console

   ``<GitHub Repository>/boards/ip``


The project files for the logictools overlay(s) can be found here:

.. code-block:: console

   ``<GitHub Repository>/boards/<board>/logictools``



*logictools* overlay

Operation
--------------------

The FSM, Boolean, and Pattern generators operate in a similar way, and will be considered together. The Trace Analyzer will be considered separately.

The state diagram below shows the primary states and transitions suppoirted by the logictools API.  Any one of the three generators exists in one of three, mutually-exclusive states.  These states are RESET, READY, and RUNNING as shown by the state machine. 


logictools API state diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../../images/logictools_API_FSM.png
   :height: 100px
   :width: 200px
   :scale: 75%
   :align: center


**RESET state**

The Interface Switch is attached to the external IO pins. Initially, all IO accessible to the logictools overlay are configured as IO pins and pulled high via a weak pull-up resistor. This prevents the inadvertent driving of any external circuitry that is connected to those pins before the logictools overlay has been configured. 

WithinThe Pattern Generator contains BRAM to store the pattern to be generated. The BRAM is configured with zeros initially. 

Similarly, the FSM Generator configuration is stored in a BRAM which is also configured with zeros initially. 

The Boolean Generator is initially set to <>

**Setup** 

Each block must be configured using the ``setup()`` method before it can be used. This defines a configuration for the block, and the configuration for the Interface Switch to connect the external IO to the builder. Note that the configuration is defined, but the IO are not connected during setup. 


**Running**

Once a block has been setup, it can be run. The external IO are connected to the block though the interface switch, and the hardware block will start operating. 

Running will start the block running in continuous mode by default. This is the only mode for the Boolead Generator. 

In continuous mode, the Pattern Generator generates its pattern continuously, looping back to the start when it reaches the end of the pattern. The FSM Generator will continue to run until it is stopped. 

The Pattern Generator can also be run in single-shot mode. In this mode, it will generate its pattern once. 
The primary transitions for a generator block correspond to its principal methods.

Generator Methods
^^^^^^^^^^^^^^^^^^^^^^

Each generator has the following methods:

* ``setup()`` - configure the block and prepare Interface Switch configuration
* ``run()`` - connect IO and start the block running
* ``stop()`` - disconnect IO and stop the block running
* ``reset()`` - clear the block configuration
* ``trace()`` - enable/disable trace


Logictools Generators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. code-block:: Python

      import logictools
      
      fsm = logictools.StateMachineGenerator()
      
      fsm.setup(fsm_spec)
      



Any one of these blocks, or any combination can be configured and run synchronously. 



Stepping
^^^^^^^^^^^^^^^^^^

Instead of running, the Pattern Generator and FSM Generator can also be single stepped. 

When stepping the Pattern Generator, it will step until the end of the configured pattern. It will not loop back to the beginning. 

The FSM Generator can be single stepped indefinitely. 

Stopping
^^^^^^^^^^^^^^^^^^

If a block is running, it must be stopped before running or stepping it again. Once a builder is stopped, its outputs are disconnected from the IO.

Trace
^^^^^^^^^^^^^^^^^^^

Trace is enabled by default for each block. i.e. the Trace Analyzer will capture trace data for all connected blocks by default. The ``trace()`` method enables/disables the Trace Analyzer for that block.  

 
Pattern Generator
-------------------------------

The Pattern Generator allows arbitrary patterns to be streamed to IO. This can be used to test external peripherals, or as a way to drive external device. Patterns of up to 8K can be described in a JSON (text format), stored in FPGA BRAM, and streamed out to the interface pins on demand.  


Waveform notation
^^^^^^^^^^^^^^^^^^

Waveforms can be defined with the following notation:

.. code-block:: console

   l: low
   h: high
   .: no change

The pattern can be repeated a number of times by "multiplying". E.g. the following will toggle the signal low-high 64 times.  

.. code-block:: console

   *'lh' /* 64* 

The length of patterns will be automatically padded to match the length of the longest specified pattern. 

Example 
^^^^^^^^^^^^^^^^^^

.. code-block:: Python

   loopback_test = {'signal': [
        ['stimulus',
            {'name': 'clk0',  'pin': 'D0', 'wave': 'lh' * 64},
            {'name': 'clk1',  'pin': 'D1', 'wave': 'l.h.' * 32},
            {'name': 'clk2',  'pin': 'D2', 'wave': 'l...h...' * 16},      
        ['analysis',
            {'name': 'clk0',  'pin': 'D0'},
            {'name': 'clk1',  'pin': 'D1'},
            {'name': 'clk2',  'pin': 'D2'}]], 

        'foot': {'tock': 1, 'text': 'Loopback Test'},
        'head': {'tick': 1, 'text': 'Loopback Test'}}

   # show start, stop, continuous, one shot


FSM Generator
--------------------------------------

The FSM Generator allows finite state machines to be specified from Python in a JSON format. The JSON description can be passed to the ``setup()`` method which will program the overlay to implement the FSM. The FSM states can be graphed and displayed inside a Jupyter Notebook. 

The FSM supports up to 20 pins that can be used in any combination of inputs or outputs. Up to xxx states are supported. 

The specification for the finite state machine is a list of inputs, outputs, states, and transitions. 

Input and outputs are listed as tuples, specifying a pin and label for the pin. 

.. code-block:: Python

    ('reset','D0')
    
Valid pins are found in the interface specification:

Transitions  are specified by defining the input bits, '01' in the following example, the current state, 'S0', the next state, 'S5', and the output bits '011'.
    
.. code-block:: Python

    ['01', 'S0', 'S5', '000']
    

Wildcards for inputs '-' and for states '\*' can be used. 

.. code-block:: Python

    ['-1', '*', 'S5', '000']

Specifying ‘use_state_bits=True’ will output the state to unassigned bits on the interface. If there are no unused pins available, the last few output pins will be automatically overwritten to show state bits instead. 

Example 
^^^^^^^^^^^^^^^^^^^^^
     
.. code-block:: Python

   fsm_spec = {'inputs': [('reset','D0'), ('direction','D1')],
               'outputs': [('bit2','D3'), ('bit1','D4'), ('bit0','D5')],
               'states': ['S0', 'S1', 'S2', 'S3', 'S4', 'S5'],
               'transitions': [['00', 'S0', 'S1', '000'],
                               ['01', 'S0', 'S5', '000'],
                               ['00', 'S1', 'S2', '001'],
                               ['01', 'S1', 'S0', '001'],
                               ['00', 'S2', 'S3', '010'],
                               ['01', 'S2', 'S1', '010'],
                               ['00', 'S3', 'S4', '011'],
                               ['01', 'S3', 'S2', '011'],
                               ['00', 'S4', 'S5', '100'],
                               ['01', 'S4', 'S3', '100'],
                               ['00', 'S5', 'S0', '101'],
                               ['01', 'S5', 'S4', '101'],
                               ['1-', '*',  'S0', '']]}
   
   # show start, stop, continuous, one shot
   
display_graph()

Boolean Generator
-------------------------------------------

The Boolean Generator supports Boolean functions of one up to five inputs on each output pin. AND, OR, NOT, and XOR operators are supported.

Example 
^^^^^^^^^^^^^^^^^^^^^

Combinatorial Boolean expressions can be defined in a Python list using the expressions & (AND), | (OR), ! (NOT), ^ (XOR). The expression list also defines the input and output pins. 
 
The following list defines four combinatorial functions on pins D8-11, which are built using combinatorial functions made up of inputs from pins D0-D3. Any pin assigned a value is an output, and any pin used as a parameter in the expression is an input. If a pin is defined as an output, it cannot be used as an input.


.. code-block:: Python

   from logictools import BoolGenerator

   bg = BoolGenerator
   function_specs = ['D3 = D0 ^ D1 ^ D2',
                   'D7 = D3 & D4 & D5']
                   
   function_specs.append('D11 = D12 + D14')

Where D<0-20> are the available IO pins. 

The function configurations can also be labelled:

.. code-block:: Python

   function_specs = {'f1': 'D3 = D0 ^ D1 ^ D2',
                     'f2': 'D7 = D3 & D4 & D5'}
                   
   function_specs['f3'] = 'D11 = D12 + D14'

Once the expressions have been defined, they can be passed to the BooleanGenerator function.

.. code-block:: Python

   bg.setup(function_specs)


.. code-block:: Python

   bg.run() # run continuously

To reconfigure the Boolean Generator, or to disconnect the IO pins, stop it. 

.. code-block:: Python

   bg.stop()


Trace Analyzer
-------------------------------------------

The trace analyzer is connected to the external interface and can capture input or output signals on each pin and stream the data to DRAM. The trace analyzer supports streaming of up to 8MB of data to DRAM in one burst. Once the data is in memory it can be analyzed in Python. 

There are a number of Python packages that could be used to analyze or process the data. WaveDrom and SigRok are two packages that can be used to processing and displaying waveforms in a Jupyter Notebook. Both these packages are included as part of the PYNQ image. 


By default the Trace Analyzer is on for all IO. Trace can be enabled/disabled for each block using the corresponding functions. 

* ``trace_on()``
* ``trace_off()``


Example 
^^^^^^^^^^^^^^^^^^^^

