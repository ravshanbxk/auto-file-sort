from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent
from watchdog.events import FileSystemMovedEvent

import os
import time

class ScreenshotHandler(FileSystemEventHandler):
	dest_folder = 'screenshots'

	# def on_created(self, event):
	# 	if event.src_path.endswith('.png'):
	# 		path = event.src_path.split('/')
	# 		file_name = path[-1]

	# 		path = path[:-1]
	# 		directory = ''
	# 		for part in path:
	# 			directory += part + '/'

	# 		if file_name[0] == '.':
	# 			file_name = file_name[1:]
	# 			time.sleep(1)

	# 		if file_name.startswith('Screenshot 20'):
	# 			if os.path.exists(directory + file_name):
	# 				new_directory = directory + 'screenshots/'
	# 				if not os.path.exists(new_directory):
	# 					os.mkdir(new_directory);

	# 				os.rename(directory + file_name, new_directory + file_name)

	def on_moved(self, event):
		if event.dest_path.startswith('/Users/rav/Desktop/Screenshot 20') and event.dest_path.endswith('.png'):
			# print('passed first if')
			path = event.dest_path.split('/')
			file_name = path[-1]

			path = path[:-1]
			directory = ''
			for part in path:
				directory += part + '/'
			
			new_directory = directory + 'screenshots/'
			# print('new directory: ' + new_directory)
			if not os.path.exists(new_directory):
				os.mkdir(new_directory);

			os.rename(directory + file_name, new_directory + file_name)

	# def on_any_event(self, event):
	# 	print(f'Any event called for "{event.event_type}" on path ' + event.src_path)
	# 	if isinstance(event, FileSystemMovedEvent):
	# 		print(f'--> to {event.dest_path}')

# class MyObserver(Observer):
# 	def stop(self):
# 		print('stop called')
# 		super().stop()

event_handler = ScreenshotHandler()
observer = Observer()
observer.schedule(event_handler, '/Users/rav/Desktop/')
observer.start()

try:
	while observer.is_alive():
		observer.join(1)
finally:
	observer.stop()
	observer.join()