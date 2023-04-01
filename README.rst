================
BADE Python example project
================

Requirements
=======

Use Python 3.10 or newer

Installation
=======

Install from GitHub

.. code-block:: text

    git clone https://github.com/bavodenys/python_project_example.git
    cd python_project_example
    pip install .


Example
=======

.. code-block:: python

	from bade.speedconversion import kph_to_knots

	if __name__ == "__main__":
		windspeed_kph = 30
		windspeed_knots = kph_to_knots(windspeed_kph)
		print(f"{windspeed_kph} kph = {windspeed_knots} kt")




Sub-heading
-----------


