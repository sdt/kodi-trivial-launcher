This is a bit of an experiment. I want to be able to launch EmulationStation
from within Kodi, but don't yet want to install Advanced Launcher.

The idea is to have a script that will do this:

```
# /usr/local/bin/launch-emulationstation
# Kodi runs as a systemd service on my htpc.
systemctl --user stop kodi
xinit /usr/bin/emulationstation -- -nocursor :0
systemctl --user start kodi
```

And have that triggered from a menu item in 720p/Home.xml, like so:

```
<item id="666">
	<label>Something!</label>
	<onclick>RunScript("script.trivial.launcher", "/usr/local/bin/launch-emulationstation")</onclick>
	<icon>-</icon>
	<thumb>-</thumb>
</item>
```

We'll see how it goes.
