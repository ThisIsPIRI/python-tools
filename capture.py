import cv2
import functools
import gi
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk
import numpy as np
import sched
import time

def pixbuf_to_array(pixbuf):
	"""
	Converts a GDK PixBuf to numpy array.

	:param gtk.gdk.PixBuf pixbuf: The PixBuf to convert.
	:return: An array containing the raw pixels in ver-hor-rgb order.
	"""
	return np.frombuffer(pixbuf.get_pixels(), dtype=np.uint8).reshape(pixbuf.get_height(), pixbuf.get_width(), pixbuf.get_n_channels())

def get_pixbuf(window):
	return Gdk.pixbuf_get_from_window(window, *window.get_geometry())

def get_active_window():
	return Gdk.get_default_root_window().get_screen().get_active_window()

def repeat(func, interval, *args, **kwargs):
	"""
	Repeatedly calls a function. Blocks. Return True from the function to stop the repetition.

	:param func: The function to call.
	:param float interval: The interval between calls in seconds. The actual interval will NOT be exactly equal to this.
	:param args: The positional arguments to pass into func.
	:param kwargs: The keyword arguments to pass into func.
	"""
	scheduler = sched.scheduler(time.time, time.sleep)
	def repeat_decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			started = time.time()
			stopped = func(*args, **kwargs)
			if not stopped:
				scheduler.enter(interval - (time.time() - started), 1, wrapper, args, kwargs)
		return wrapper
	scheduler.enter(interval, 1, repeat_decorator(func), args, kwargs)
	scheduler.run()

def mirror(window, refresh_interval=0.03):
	"""
	Mirrors a GDK Window in an OpenCV image viewer.

	:param gtk.gdk.Window window: The Window to mirror.
	:param float refresh_interval: The interval between updates in seconds. The actual interval will NOT be exactly equal to this.
	"""
	def show_frame():
		arr = pixbuf_to_array(get_pixbuf(window))
		cv2.imshow("image", cv2.cvtColor(arr, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(1) & 0xFF == ord('q'):
			return
	repeat(show_frame, refresh_interval)
