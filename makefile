
run: main.py display.py draw.py matrix.py parser.py
	python my_Script_generator.py
	python main.py

clean:
	rm *.pyc
	rm *~
