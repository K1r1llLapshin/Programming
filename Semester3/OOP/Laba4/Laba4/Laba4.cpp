#include <iostream>
#include "Key.h"
#include "Keyboard.h"
int main()
{
	Key H, e, l, o, w, r, d, tab, caps, v;

	H.setKey("H", Press);
	e.setKey("e", Press);
	l.setKey("l", Press);
	o.setKey("o", Press);
	w.setKey("w", Press);
	r.setKey("r", Press);
	d.setKey("d", Press);
	tab.setKey("tab", Tab);
	caps.setKey("caps", Caps);
	v.setKey("v", VolumeUp);

	Keyboard keybord;
	
	keybord.setKeyboard(H);
	keybord.setKeyboard(e);
	keybord.setKeyboard(l);
	keybord.setKeyboard(o);
	keybord.setKeyboard(w);
	keybord.setKeyboard(r);
	keybord.setKeyboard(d);
	keybord.setKeyboard(caps);
	keybord.setKeyboard(tab);

	keybord.pressKey(H);
	keybord.pressKey(e);
	keybord.pressKey(l);
	keybord.pressKey(l);
	keybord.pressKey(o);
	keybord.pressKey(caps);
	keybord.pressKey(w);
	keybord.pressKey(o);
	keybord.undo();
	keybord.pressKey(r);
	keybord.pressKey(l);
	keybord.pressKey(d);
	keybord.pressKey(v);
	keybord.pressKey(v);
	v.overrideKey(VolumeDown);
	keybord.pressKey(v);
	v.overrideKey(VolumeUp);
	keybord.pressKey(v);
	keybord.pressKey(caps);
	keybord.pressKey(tab);
	keybord.pressKey(H);
	keybord.pressKey(e);
	keybord.pressKey(l);
	keybord.pressKey(l);
	keybord.pressKey(o);
	keybord.undo();
	keybord.pressKey(w);
	keybord.pressKey(o);
	keybord.pressKey(r);
	keybord.pressKey(l);
	keybord.pressKey(d);
}

