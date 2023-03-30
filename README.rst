================
BADE Python example project
================

Requirements
=======

Use Python 3.10 or newer

Installation
=======

Install from BitBucket

.. code-block:: text

    git clone git clone https://github.com/bavodenys/python_project_example.git
    cd python_project_example
    pip install .


Example
=======

.. code-block:: python

	from bade.speedconversion import kph_to_mph

	if __name__ == "__main__":
		speed_kph = 30
		speed_mph = kph_to_mph(speed_kph)
		print(f"{speed_kph} kph = {speed_mph} mph")




Sub-heading
-----------


