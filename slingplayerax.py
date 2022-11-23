# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)]
# From type library '{7C9EBD5F-0D6C-4071-8F38-97875DDF3CD3}'
# On Mon Nov 21 22:22:24 2022
'SlingPlayerAX 1.0 Type Library'
makepy_version = '0.5.01'
python_version = 0x30a08f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{7C9EBD5F-0D6C-4071-8F38-97875DDF3CD3}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IBoxIdentity(DispatchBaseClass):
	'IBoxIdentity Interface'
	CLSID = IID('{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}')
	coclass_clsid = IID('{00774808-0A96-45CA-A55B-B608BEE33B6E}')

	def Assign(self, pBox=defaultNamedNotOptArg):
		'method Assign'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((9, 1),),pBox
			)

	def LoadDeviceConfig(self):
		'method LoadDeviceConfig'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def SetName(self, sDevName=defaultNamedNotOptArg):
		'method SetName'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((8, 1),),sDevName
			)

	def SetProductID(self, nProductID=defaultNamedNotOptArg):
		'method SetProductID'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((19, 1),),nProductID
			)

	_prop_map_get_ = {
		"ConnectionString": (20, 2, (8, 0), (), "ConnectionString", None),
		"DiscoveryState": (18, 2, (19, 0), (), "DiscoveryState", None),
		"FinderID": (1, 2, (8, 0), (), "FinderID", None),
		"GetPassword": (9, 2, (8, 0), (), "GetPassword", None),
		"IPAddress": (2, 2, (8, 0), (), "IPAddress", None),
		"Initialised": (8, 2, (3, 0), (), "Initialised", None),
		"IsAvailable": (17, 2, (3, 0), (), "IsAvailable", None),
		"IsConfigured": (16, 2, (3, 0), (), "IsConfigured", None),
		"IsDiscovered": (15, 2, (3, 0), (), "IsDiscovered", None),
		"IsSaved": (14, 2, (3, 0), (), "IsSaved", None),
		"Name": (12, 2, (8, 0), (), "Name", None),
		"Password": (6, 2, (8, 0), (), "Password", None),
		"Port": (3, 2, (18, 0), (), "Port", None),
		"ProductID": (7, 2, (19, 0), (), "ProductID", None),
		"Save": (19, 2, (3, 0), (), "Save", None),
		"UseIPPort": (4, 2, (3, 0), (), "UseIPPort", None),
		"Username": (5, 2, (8, 0), (), "Username", None),
	}
	_prop_map_put_ = {
		"ConnectionString": ((20, LCID, 4, 0),()),
		"FinderID": ((1, LCID, 4, 0),()),
		"IPAddress": ((2, LCID, 4, 0),()),
		"Password": ((6, LCID, 4, 0),()),
		"Port": ((3, LCID, 4, 0),()),
		"Save": ((19, LCID, 4, 0),()),
		"UseIPPort": ((4, LCID, 4, 0),()),
		"Username": ((5, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBoxIdentityEnum(DispatchBaseClass):
	'IBoxIdentityEnum Interface'
	CLSID = IID('{05FA90E7-297F-4ED9-B041-BCF37C14CB30}')
	coclass_clsid = IID('{EFBEECAF-71BD-4D66-A184-51B9F5252698}')

	# Result is of type IBoxIdentity
	# The method At is actually a property, but must be used as a method to correctly pass the arguments
	def At(self, ulIndex=defaultNamedNotOptArg):
		'property At'
		ret = self._oleobj_.InvokeTypes(2, LCID, 2, (9, 0), ((19, 1),),ulIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'At', '{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}')
		return ret

	# Result is of type IBoxIdentity
	# The method FinderID is actually a property, but must be used as a method to correctly pass the arguments
	def FinderID(self, strFinderId=defaultNamedNotOptArg):
		'Get the box by providing the finder id'
		ret = self._oleobj_.InvokeTypes(3, LCID, 2, (9, 0), ((8, 0),),strFinderId
			)
		if ret is not None:
			ret = Dispatch(ret, 'FinderID', '{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (19, 0), (), "Count", None),
		"Length": (4, 2, (19, 0), (), "Length", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (19, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IBoxPropsAX(DispatchBaseClass):
	'IBoxPropsAX Interface'
	CLSID = IID('{DE5F0E99-42D7-4724-AD5F-1B46910B68E1}')
	coclass_clsid = IID('{DE947688-953F-4122-A9AE-1365AE038FED}')

	def CheckLebowskiSupported(self, sLeboType=defaultNamedNotOptArg):
		'method CheckLebowskiSupported'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (3, 0), ((18, 1),),sLeboType
			)

	def IsCapable(self, capability=defaultNamedNotOptArg):
		'Check box capability'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (3, 0), ((3, 0),),capability
			)

	_prop_map_get_ = {
		"ConnectionSessionID": (35, 2, (8, 0), (), "ConnectionSessionID", None),
		"Country": (27, 2, (19, 0), (), "Country", None),
		"CountryCode": (37, 2, (19, 0), (), "CountryCode", None),
		"DefaultCountryCode": (29, 2, (3, 0), (), "DefaultCountryCode", None),
		"DestinationIP": (40, 2, (8, 0), (), "DestinationIP", None),
		"DestinationPort": (41, 2, (3, 0), (), "DestinationPort", None),
		"DeviceIPAddress": (44, 2, (8, 0), (), "DeviceIPAddress", None),
		"FirmwareReleaseDate": (7, 2, (8, 0), (), "FirmwareReleaseDate", None),
		"FirmwareVersion": (6, 2, (8, 0), (), "FirmwareVersion", None),
		"GatewayIP": (11, 2, (8, 0), (), "GatewayIP", None),
		"HWBuildVersion": (33, 2, (3, 0), (), "HWBuildVersion", None),
		"HWMajorVersion": (31, 2, (3, 0), (), "HWMajorVersion", None),
		"HWMinorVersion": (32, 2, (3, 0), (), "HWMinorVersion", None),
		"HardwareVersion": (4, 2, (8, 0), (), "HardwareVersion", None),
		"IPAddress": (9, 2, (8, 0), (), "IPAddress", None),
		"IPSubnetMask": (10, 2, (8, 0), (), "IPSubnetMask", None),
		"IPType": (8, 2, (8, 0), (), "IPType", None),
		"IRBlasterVersion": (5, 2, (8, 0), (), "IRBlasterVersion", None),
		"IsConfigured": (36, 2, (19, 0), (), "IsConfigured", None),
		"IsLocal": (30, 2, (3, 0), (), "IsLocal", None),
		"IsRegistered": (21, 2, (3, 0), (), "IsRegistered", None),
		"LastConflictedIP": (13, 2, (8, 0), (), "LastConflictedIP", None),
		"LastInputIndex": (39, 2, (3, 0), (), "LastInputIndex", None),
		"LastUpdated": (28, 2, (8, 0), (), "LastUpdated", None),
		"MAC": (1, 2, (8, 0), (), "MAC", None),
		"MSGServer": (25, 2, (8, 0), (), "MSGServer", None),
		"MSGServerPorts": (26, 2, (19, 0), (), "MSGServerPorts", None),
		"Name": (2, 2, (8, 0), (), "Name", None),
		"Ping": (23, 2, (3, 0), (), "Ping", None),
		"PingPeriod": (24, 2, (19, 0), (), "PingPeriod", None),
		"Port": (12, 2, (19, 0), (), "Port", None),
		"ProductID": (3, 2, (19, 0), (), "ProductID", None),
		"RegistrationPeriod": (22, 2, (19, 0), (), "RegistrationPeriod", None),
		"RelayManagerEndUrl": (43, 2, (8, 0), (), "RelayManagerEndUrl", None),
		"RelayManagerStartUrl": (42, 2, (8, 0), (), "RelayManagerStartUrl", None),
		"RemoteConfiguration": (18, 2, (3, 0), (), "RemoteConfiguration", None),
		"SlingServerIP": (19, 2, (8, 0), (), "SlingServerIP", None),
		"SlingServerPort": (20, 2, (19, 0), (), "SlingServerPort", None),
		"UPNPIGDRouterIP": (14, 2, (8, 0), (), "UPNPIGDRouterIP", None),
		"UPNPIGDRouterPort": (15, 2, (19, 0), (), "UPNPIGDRouterPort", None),
		"UPNPURI": (16, 2, (8, 0), (), "UPNPURI", None),
		"WANAccess": (17, 2, (3, 0), (), "WANAccess", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChannel(DispatchBaseClass):
	'IChannel Interface'
	CLSID = IID('{4192D38F-9410-41EF-AAE0-9F850B1A689F}')
	coclass_clsid = IID('{59E91392-CAD0-4DB9-84A8-4A57C6AFDF1E}')

	_prop_map_get_ = {
		"ChannelAsString": (4, 2, (8, 0), (), "ChannelAsString", None),
		"Frequency": (3, 2, (4, 0), (), "Frequency", None),
		"MajorChannelNo": (1, 2, (19, 0), (), "MajorChannelNo", None),
		"MinorChannelNo": (2, 2, (2, 0), (), "MinorChannelNo", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IClosedCaptionAX(DispatchBaseClass):
	'IClosedCaptionAX Interface'
	CLSID = IID('{B68271A5-7166-476C-9BE8-D6B9C5372C90}')
	coclass_clsid = IID('{16E1B18E-55D9-4191-8C83-F0404CE38443}')

	def SetCCDefaults(self):
		'method SetCCDefaults'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def SetServiceChannel(self, nChannel=defaultNamedNotOptArg):
		'method SetServiceChannel'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((3, 1),),nChannel
			)

	_prop_map_get_ = {
		"BGColor": (8, 2, (3, 0), (), "BGColor", None),
		"BGOpacity": (9, 2, (3, 0), (), "BGOpacity", None),
		"FontColor": (2, 2, (3, 0), (), "FontColor", None),
		"FontEdgeColor": (6, 2, (3, 0), (), "FontEdgeColor", None),
		"FontEdgeStyle": (5, 2, (3, 0), (), "FontEdgeStyle", None),
		"FontOpacity": (7, 2, (3, 0), (), "FontOpacity", None),
		"FontSize": (3, 2, (3, 0), (), "FontSize", None),
		"FontStyle": (4, 2, (3, 0), (), "FontStyle", None),
		"Visible": (1, 2, (3, 0), (), "Visible", None),
		"WindowColor": (12, 2, (3, 0), (), "WindowColor", None),
	}
	_prop_map_put_ = {
		"BGColor": ((8, LCID, 4, 0),()),
		"BGOpacity": ((9, LCID, 4, 0),()),
		"FontColor": ((2, LCID, 4, 0),()),
		"FontEdgeColor": ((6, LCID, 4, 0),()),
		"FontEdgeStyle": ((5, LCID, 4, 0),()),
		"FontOpacity": ((7, LCID, 4, 0),()),
		"FontSize": ((3, LCID, 4, 0),()),
		"FontStyle": ((4, LCID, 4, 0),()),
		"Visible": ((1, LCID, 4, 0),()),
		"WindowColor": ((12, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMyMedia(DispatchBaseClass):
	'IMyMedia Interface'
	CLSID = IID('{14D4BE41-CBC6-4030-BA7B-C42CF18BD030}')
	coclass_clsid = IID('{9B3E9F8A-72A6-4B41-9432-1B0F8D1EDD2B}')

	def ChangeContent(self, playURL=defaultNamedNotOptArg, offset=defaultNamedNotOptArg, Flush=defaultNamedNotOptArg):
		'Change the current playing content'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 1)),playURL
			, offset, Flush)

	def Pause(self, Flush=defaultNamedNotOptArg):
		'Pause the current Video PS'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((3, 1),),Flush
			)

	def Resume(self, offset=defaultNamedNotOptArg, Flush=defaultNamedNotOptArg):
		'Resume currently paused video'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((8, 1), (3, 1)),offset
			, Flush)

	def Seek(self, offset=defaultNamedNotOptArg, Flush=defaultNamedNotOptArg):
		'Seek video data'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (24, 0), ((8, 1), (3, 1)),offset
			, Flush)

	def Start(self, playURL=defaultNamedNotOptArg, offset=defaultNamedNotOptArg):
		'Send MM play command'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1), (8, 1)),playURL
			, offset)

	def Stop(self, bookmark=defaultNamedNotOptArg, Flush=defaultNamedNotOptArg):
		'Stop MM playback'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((8, 1), (3, 1)),bookmark
			, Flush)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPlayerPropsAX(DispatchBaseClass):
	'IPlayerPropsAX Interface'
	CLSID = IID('{9CEBC8CF-8907-433D-B1D7-41FE2EB1DCDB}')
	coclass_clsid = IID('{3B2CBA5C-8D99-4A1D-A834-6E1543784FE4}')

	def Flush(self, bFlushBox=defaultNamedNotOptArg):
		'Flush the current stream buffer'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (24, 0), ((3, 0),),bFlushBox
			)

	def GetFileLocation(self, iFileType=defaultNamedNotOptArg):
		'Get install file locations'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(41, LCID, 1, (8, 0), ((18, 1),),iFileType
			)

	def IsBoxInfoWindowVisible(self):
		'Get box information window visible status'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), (),)

	def IsFirmwareUpdateRequired(self):
		'Returns true in out param if firmware update is required'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (2, 0), (),)

	def IsStatisticsWindowVisible(self):
		'Get statistics window visible status'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), (),)

	def ProbeDXVAFromHint(self):
		'Probe system for DXVA2 capability and compatibiltiy with decoder hints provided'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(38, LCID, 1, (8, 0), (),)

	def SetFocusToVideoWindow(self):
		'method to  set keyboard focus to video window'
		return self._oleobj_.InvokeTypes(56, LCID, 1, (24, 0), (),)

	def ShowBoxInfoWindow(self, bShow=defaultNamedNotOptArg):
		'Show/Hide BoxInfo Window'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((3, 1),),bShow
			)

	def ShowStatisticsWindow(self, bShow=defaultNamedNotOptArg):
		'Show/Hide Statistics Window'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1),),bShow
			)

	_prop_map_get_ = {
		"ActualVideoHeight": (11, 2, (19, 0), (), "ActualVideoHeight", None),
		"ActualVideoWidth": (10, 2, (19, 0), (), "ActualVideoWidth", None),
		"AspectRatio": (1, 2, (19, 0), (), "AspectRatio", None),
		"AudioBitRate": (21, 2, (18, 0), (), "AudioBitRate", None),
		"AudioCodecType": (28, 2, (8, 0), (), "AudioCodecType", None),
		"AudioOnly": (43, 2, (3, 0), (), "AudioOnly", None),
		"AudioType": (44, 2, (18, 0), (), "AudioType", None),
		"Bitrate": (4, 2, (19, 0), (), "Bitrate", None),
		"BufferLength": (6, 2, (19, 0), (), "BufferLength", None),
		"BufferStatusUpdateInterval": (9, 2, (3, 0), (), "BufferStatusUpdateInterval", None),
		"CropBorder": (12, 2, (19, 0), (), "CropBorder", None),
		"CurrentFirmwareVersion": (15, 2, (8, 0), (), "CurrentFirmwareVersion", None),
		"DeviceConnectionCaps": (30, 2, (3, 0), (), "DeviceConnectionCaps", None),
		"DisplayState": (50, 2, (18, 0), (), "DisplayState", None),
		"FloatingWindow": (49, 2, (3, 0), (), "FloatingWindow", None),
		"FramesSkipped": (31, 2, (8, 0), (), "FramesSkipped", None),
		"FullScreen": (8, 2, (3, 0), (), "FullScreen", None),
		"IFrameInterval": (22, 2, (18, 0), (), "IFrameInterval", None),
		"IsClosedCaptionSupported": (46, 2, (3, 0), (), "IsClosedCaptionSupported", None),
		"IsfastHDSwitchingSupported": (51, 2, (3, 0), (), "IsfastHDSwitchingSupported", None),
		"KeyFrameAspectRatio": (53, 2, (3, 0), (), "KeyFrameAspectRatio", None),
		"LatestFirmwareVersion": (16, 2, (8, 0), (), "LatestFirmwareVersion", None),
		"Mute": (7, 2, (3, 0), (), "Mute", None),
		"OutputAspectRatio": (35, 2, (8, 0), (), "OutputAspectRatio", None),
		"PlaySpeed": (34, 2, (8, 0), (), "PlaySpeed", None),
		"Precharge": (33, 2, (8, 0), (), "Precharge", None),
		"PresentationTime": (26, 2, (19, 0), (), "PresentationTime", None),
		"RemainingStreamTime": (39, 2, (19, 0), (), "RemainingStreamTime", None),
		"RemoteControlPosition": (48, 2, (18, 0), (), "RemoteControlPosition", None),
		"RenderFramerate": (5, 2, (19, 0), (), "RenderFramerate", None),
		"SPARCSURL": (52, 2, (8, 0), (), "SPARCSURL", None),
		"ShowClosedCaption": (3, 2, (3, 0), (), "ShowClosedCaption", None),
		"StreamFramerate": (23, 2, (18, 0), (), "StreamFramerate", None),
		"StreamType": (29, 2, (19, 0), (), "StreamType", None),
		"StreamVideoHeight": (25, 2, (19, 0), (), "StreamVideoHeight", None),
		"StreamVideoWidth": (24, 2, (19, 0), (), "StreamVideoWidth", None),
		"ToggleTSB": (54, 2, (3, 0), (), "ToggleTSB", None),
		"UseInbandUI": (36, 2, (3, 0), (), "UseInbandUI", None),
		"VideoBitrate": (20, 2, (18, 0), (), "VideoBitrate", None),
		"VideoCodecType": (27, 2, (8, 0), (), "VideoCodecType", None),
		"VideoRenderType": (32, 2, (8, 0), (), "VideoRenderType", None),
		"VideoRenderTypeNum": (47, 2, (19, 0), (), "VideoRenderTypeNum", None),
		"Volume": (2, 2, (19, 0), (), "Volume", None),
	}
	_prop_map_put_ = {
		"AspectRatio": ((1, LCID, 4, 0),()),
		"AudioOnly": ((43, LCID, 4, 0),()),
		"AudioType": ((44, LCID, 4, 0),()),
		"BufferLength": ((6, LCID, 4, 0),()),
		"BufferStatusUpdateInterval": ((9, LCID, 4, 0),()),
		"CropBorder": ((12, LCID, 4, 0),()),
		"DisableIR": ((37, LCID, 4, 0),()),
		"ExtendedStreamTime": ((40, LCID, 4, 0),()),
		"FloatingWindow": ((49, LCID, 4, 0),()),
		"FullScreen": ((8, LCID, 4, 0),()),
		"Mute": ((7, LCID, 4, 0),()),
		"RemoteControlPosition": ((48, LCID, 4, 0),()),
		"ShowClosedCaption": ((3, LCID, 4, 0),()),
		"ToggleNativeInputHandling": ((55, LCID, 4, 0),()),
		"ToggleTSB": ((54, LCID, 4, 0),()),
		"UseInbandUI": ((36, LCID, 4, 0),()),
		"Volume": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRemoteControlAX(DispatchBaseClass):
	'IRemoteControlAX Interface'
	CLSID = IID('{626B8C4A-383B-4781-ACC2-D8B661909D43}')
	coclass_clsid = IID('{DCEA4309-3D50-4991-AA21-18BE5A9571C6}')

	def ChannelDown(self):
		'method ChannelDown'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def ChannelLast(self):
		'method ChannelLast'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def ChannelUp(self):
		'method ChannelUp'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	def GetRemoteByIndex(self, byIndex=defaultNamedNotOptArg):
		'Returns remote based on the provided index'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(11, LCID, 1, (8, 0), ((3, 1),),byIndex
			)

	def NotiyUserInput(self, bEnable=defaultNamedNotOptArg):
		'method NotiyUserInput'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((3, 1),),bEnable
			)

	def PositionRemote(self, left=defaultNamedNotOptArg, top=defaultNamedNotOptArg):
		'method PositionRemote'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), ((3, 1), (3, 1)),left
			, top)

	def SelectRemote(self, ulIndex=defaultNamedNotOptArg):
		'Loads Selected Remote'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),ulIndex
			)

	def SendCommand(self, lCode=defaultNamedNotOptArg):
		'method SendCommand'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),lCode
			)

	def SetChannel(self, szChannel=defaultNamedNotOptArg):
		'method SetChannel'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((8, 1),),szChannel
			)

	def ToggleMove(self, bEnable=defaultNamedNotOptArg):
		'method ToggleMove'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1),),bEnable
			)

	_prop_map_get_ = {
		"Current": (5, 2, (3, 0), (), "Current", None),
		"GetRemoteCount": (4, 2, (17, 0), (), "GetRemoteCount", None),
		"IsAvailable": (2, 2, (3, 0), (), "IsAvailable", None),
		"RemoteGUID": (13, 2, (8, 0), (), "RemoteGUID", None),
		"Show": (1, 2, (3, 0), (), "Show", None),
		"Width": (14, 2, (3, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"RemoteServicesURL": ((3, LCID, 4, 0),()),
		"Show": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISQAParamsAX(DispatchBaseClass):
	'ISQAParamsAX Interface'
	CLSID = IID('{965C70F8-62FE-4732-A338-1B709172B2F9}')
	coclass_clsid = IID('{C95D46F1-30C7-4889-AFB8-1FF19A207AF5}')

	def LogBadVideo(self):
		'LogBadVideo for Logging to CSV upon button click'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"BitrateIndex": (5, 2, (3, 0), (), "BitrateIndex", None),
		"NetworkHealthIndex": (2, 2, (3, 0), (), "NetworkHealthIndex", None),
		"PlaybackHealthIndex": (3, 2, (3, 0), (), "PlaybackHealthIndex", None),
		"PrechargeIndex": (4, 2, (3, 0), (), "PrechargeIndex", None),
		"SQAEnabledCheck": (7, 2, (3, 0), (), "SQAEnabledCheck", None),
		"SystemCapsIndex": (6, 2, (3, 0), (), "SystemCapsIndex", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISUAAX(DispatchBaseClass):
	'ISUAAX Interface'
	CLSID = IID('{DE89D4A9-880F-4536-9F80-CC54CCB93D43}')
	coclass_clsid = IID('{D79B47D1-384C-4D00-B7A3-023D4F9655B3}')

	def Apply(self):
		'method Apply - Saves the current changes to Slingbox'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	def AutoUploadIRBinFile(self, strURLName=defaultNamedNotOptArg):
		'Auto IR bin file will be uploaded into box.'
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), ((8, 1),),strURLName
			)

	def Cancel(self):
		'method Cancel - Cancel all the changes made'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	def ChangeChannel(self, Channel=defaultNamedNotOptArg):
		'Changes channel to one specified in the argument.'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((8, 1),),Channel
			)

	def CompareCredentials(self, nIndex=defaultNamedNotOptArg, inStrData=defaultNamedNotOptArg):
		'Compare credentials for admin and guest passwords'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (3, 0), ((3, 1), (8, 1)),nIndex
			, inStrData)

	def ControlInternalIRBlast(self, bEnableInternal=defaultNamedNotOptArg):
		'method ControlInternalIRBlast'
		return self._oleobj_.InvokeTypes(33, LCID, 1, (24, 0), ((3, 1),),bEnableInternal
			)

	def End(self):
		'Complete SUA'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def FirmwareUpload(self, fileName=defaultNamedNotOptArg, bRestartAfterUpdate=defaultNamedNotOptArg):
		'Firmware bin file will be uploaded to the box'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), ((8, 1), (3, 1)),fileName
			, bRestartAfterUpdate)

	# Result is of type IChannel
	def GetChannelAt(self, ulIndex=defaultNamedNotOptArg):
		'Get the channel information based on the specified index. It will return channel interface'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((19, 1),),ulIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetChannelAt', '{4192D38F-9410-41EF-AAE0-9F850B1A689F}')
		return ret

	def GetLatestRemotes(self):
		'Check if latest remote controls are available, if so then download them'
		return self._oleobj_.InvokeTypes(25, LCID, 1, (24, 0), (),)

	def GetPossibleDeviceInfo(self, ulIndex=defaultNamedNotOptArg):
		'Get possible device that can be connected to the current input'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (19, 0), ((19, 1),),ulIndex
			)

	def GetProperty(self, nPropId=defaultNamedNotOptArg):
		'GetProperty is used to get various properties on Slingbox'
		return self._ApplyTypes_(1, 1, (12, 0), ((3, 0),), 'GetProperty', None,nPropId
			)

	def HDMI_ControlHDCP(self, lEnableHDCP=defaultNamedNotOptArg):
		'method HDMI_ControlHDCP'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), ((3, 1),),lEnableHDCP
			)

	def HDMI_DisableHDMIOnPlaceShifting(self, lDisableReason=defaultNamedNotOptArg, lAssociatedInputIndex=defaultNamedNotOptArg):
		'method HDMI_DisableHDMIOnPlaceShifting'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), ((3, 1), (3, 1)),lDisableReason
			, lAssociatedInputIndex)

	def HDMI_ResetDisableHDMIOnPlaceShifting(self):
		'method HDMI_ResetDisableHDMIOnPlaceShifting'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), (),)

	def HDMI_SoftControlHDMI(self, lEnableHDMI=defaultNamedNotOptArg):
		'method HDMI_SoftControlHDMI'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (24, 0), ((3, 1),),lEnableHDMI
			)

	def InitPossibleDeviceTypes(self, CountryInfo=defaultNamedNotOptArg):
		'Init possible device that can be connected to the current input'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (24, 0), ((8, 1),),CountryInfo
			)

	def IsModified(self):
		'Checks if the data in the current state is modified.'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), (),)

	def LoadKeyMap(self):
		'Load Keymap for current input'
		return self._oleobj_.InvokeTypes(28, LCID, 1, (24, 0), (),)

	def MoveToState(self, nState=defaultNamedNotOptArg):
		'method MoveToState -  Moves from one state to another'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((2, 0),),nState
			)

	def RVDisable(self):
		'Disable configuration for remote viewing'
		return self._oleobj_.InvokeTypes(22, LCID, 1, (24, 0), (),)

	def RVSkip(self):
		'Skip configuration for remote viewing'
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), (),)

	def RVStartAutomaticConfiguration(self):
		'Automatic configuration for remote viewing'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), (),)

	def RVStartManualConfiguration(self):
		'Manual configuration for remote viewing'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

	def ResetInput(self, ulInputIndex=defaultNamedNotOptArg):
		'method ResetInput'
		return self._oleobj_.InvokeTypes(32, LCID, 1, (24, 0), ((19, 0),),ulInputIndex
			)

	def RestoreDefaultPictureSettings(self):
		'Restores default settings of picture configuration'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), (),)

	def Scan(self, nDetailedScan=defaultNamedNotOptArg):
		'Starts scanning on current input, also the current input must be tuner'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((2, 1),),nDetailedScan
			)

	def ScanInputVideoLock(self, uTimeoutMsec=defaultNamedNotOptArg, nInputMask=defaultNamedNotOptArg):
		'method ScanInputVideoLock'
		return self._oleobj_.InvokeTypes(34, LCID, 1, (24, 0), ((19, 1), (3, 1)),uTimeoutMsec
			, nInputMask)

	def SendIRKey(self, nIRKey=defaultNamedNotOptArg):
		"Send's IR Key to the box, can be used to test power button."
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((19, 1),),nIRKey
			)

	def SetConfigStatus(self, bSuccess=defaultNamedNotOptArg):
		'method SetConfigStatus'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((3, 1),),bSuccess
			)

	def SetProperty(self, nPropId=defaultNamedNotOptArg, inData=defaultNamedNotOptArg):
		"SetProperty set's property locally if required on Slingbox directly."
		return self._oleobj_.InvokeTypes(2, LCID, 1, (2, 0), ((3, 0), (12, 0)),nPropId
			, inData)

	def SetZipcode(self, Zipcode=defaultNamedNotOptArg):
		'method SetZipcode'
		return self._oleobj_.InvokeTypes(31, LCID, 1, (24, 0), ((8, 1),),Zipcode
			)

	def Start(self, nState=defaultNamedNotOptArg):
		'Start SUA'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((2, 0),),nState
			)

	def StartNGSBConnfig(self, bTakeOver=defaultNamedNotOptArg, nSUAState=defaultNamedNotOptArg):
		'method StartNGSBConnfig'
		return self._oleobj_.InvokeTypes(39, LCID, 1, (24, 0), ((3, 1), (2, 1)),bTakeOver
			, nSUAState)

	def UpdateLatestFirmwareFromServer(self, bRestartAfterUpdate=defaultNamedNotOptArg):
		'Check for latest firmware version available on the server, download and update if required'
		return self._oleobj_.InvokeTypes(23, LCID, 1, (24, 0), ((3, 1),),bRestartAfterUpdate
			)

	def UploadIRBinFile(self, fileName=defaultNamedNotOptArg):
		'IR bin file will be uploaded into box, current input must not be tuner.'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((8, 1),),fileName
			)

	_prop_map_get_ = {
		"CurrentState": (26, 2, (2, 0), (), "CurrentState", None),
		"PsessionID": (30, 2, (8, 0), (), "PsessionID", None),
	}
	_prop_map_put_ = {
		"PsessionID": ((30, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IServiceProxyInfo(DispatchBaseClass):
	'IServiceProxyInfo Interface'
	CLSID = IID('{B68682A7-55A6-437B-816F-EF7F2587E671}')
	coclass_clsid = IID('{F4853AF6-146C-4D56-A60D-83767F565F87}')

	def Apply(self):
		'method Apply'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Password": (2, 2, (8, 0), (), "Password", None),
		"UseBrowserProxy": (3, 2, (3, 0), (), "UseBrowserProxy", None),
		"Username": (1, 2, (8, 0), (), "Username", None),
	}
	_prop_map_put_ = {
		"Password": ((2, LCID, 4, 0),()),
		"UseBrowserProxy": ((3, LCID, 4, 0),()),
		"Username": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISlingAccountsAX(DispatchBaseClass):
	'ISlingAccountsAX Interface'
	CLSID = IID('{5FF8AF7A-B6A3-43AB-9046-8E2D6794B5F0}')
	coclass_clsid = IID('{B8085032-9FDE-43DE-8683-C6FE8379CAE5}')

	def AddEditBoxUsingIpPort(self, strIpAddress=defaultNamedNotOptArg, lPort=defaultNamedNotOptArg, strDisplayName=defaultNamedNotOptArg, strUserName=defaultNamedNotOptArg
			, strPassword=defaultNamedNotOptArg, bUseIpPort=defaultNamedNotOptArg):
		'Used to connect using IPAddress and port information'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((8, 1), (3, 1), (8, 1), (8, 1), (8, 1), (3, 1)),strIpAddress
			, lPort, strDisplayName, strUserName, strPassword, bUseIpPort
			)

	def AddorEditBox(self, strFinder=defaultNamedNotOptArg, strDevName=defaultNamedNotOptArg, strUserName=defaultNamedNotOptArg, strPassword=defaultNamedNotOptArg):
		"Add's or edit box to SlingAccounts"
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (8, 1)),strFinder
			, strDevName, strUserName, strPassword)

	def Initialize(self):
		'After setting ticket, member id and URL, call this function'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def RemoveBox(self, strFinder=defaultNamedNotOptArg):
		"Remove's box from SlingAccounts"
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((8, 1),),strFinder
			)

	def RemoveBoxUsingIpPort(self, strIpAddress=defaultNamedNotOptArg, lPort=defaultNamedNotOptArg):
		"Remove's box from SlingAccounts using IPAddress and Port"
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 1), (3, 1)),strIpAddress
			, lPort)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
		"MemberID": ((2, LCID, 4, 0),()),
		"TicketID": ((1, LCID, 4, 0),()),
		"URL": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISlingPlayer(DispatchBaseClass):
	'ISlingPlayer Interface'
	CLSID = IID('{DCF0413B-B144-42EE-AC43-62262BEA8CA1}')
	coclass_clsid = IID('{B80CD4E6-5B02-4B6C-99BE-68F1511E9549}')

	def BindUserACR(self, iID=defaultNamedNotOptArg):
		'method BindUserACR'
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), ((3, 1),),iID
			)

	def ChangeVideoInput(self, ulInputIndex=defaultNamedNotOptArg):
		'method ChangeVideoInput - provide valid input index'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((19, 1),),ulInputIndex
			)

	def Connect(self):
		"Connect will only connect to box, doesn't start streaming."
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), (),)

	def ConnectEx(self, bFastConnect=defaultNamedNotOptArg):
		"Connect will only connect to box, doesn't start streaming."
		return self._oleobj_.InvokeTypes(21, LCID, 1, (24, 0), ((3, 0),),bFastConnect
			)

	def DecryptPassword(self, szEncryptedPassword=defaultNamedNotOptArg):
		'method DecryptPassword'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(48, LCID, 1, (8, 0), ((8, 1),),szEncryptedPassword
			)

	def DecryptPasswordForNextConnection(self):
		'method DecryptPasswordForNextConnection'
		return self._oleobj_.InvokeTypes(38, LCID, 1, (24, 0), (),)

	def Discover(self):
		'Discover local sling boxes'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	def EncryptPassword(self, szPassword=defaultNamedNotOptArg):
		'method EncryptPassword'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(47, LCID, 1, (8, 0), ((8, 1),),szPassword
			)

	def FeatureSupport(self, nFeature=defaultNamedNotOptArg):
		'method FeatureSupport - Check if Feature is supported by Plugin'
		return self._oleobj_.InvokeTypes(27, LCID, 1, (3, 0), ((3, 1),),nFeature
			)

	def FireIrCommand(self, lCommand=defaultNamedNotOptArg, lExtraInfo=defaultNamedNotOptArg, lFlush=defaultNamedNotOptArg):
		'method FireIrCommand'
		return self._oleobj_.InvokeTypes(42, LCID, 1, (19, 0), ((3, 1), (3, 1), (3, 1)),lCommand
			, lExtraInfo, lFlush)

	def GetSparcsResponse(self, szFinderid=defaultNamedNotOptArg, uiRequestTimeOut=defaultNamedNotOptArg):
		'method GetSparcsResponse'
		return self._oleobj_.InvokeTypes(46, LCID, 1, (24, 0), ((8, 1), (19, 1)),szFinderid
			, uiRequestTimeOut)

	def HandleDishLoginCompletion(self):
		'method HandleDishLoginCompletion'
		return self._oleobj_.InvokeTypes(43, LCID, 1, (19, 0), (),)

	def InitACR(self, szACRKey=defaultNamedNotOptArg):
		'method InitACR'
		return self._oleobj_.InvokeTypes(53, LCID, 1, (24, 0), ((8, 1),),szACRKey
			)

	def Pause(self):
		'method Pause'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), (),)

	def Play(self):
		'method Play- Should be called if video had been paused before. The precondition to use this methos is that Player::Start has been called.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), (),)

	def RegisterFWUpgradeProgressEvent(self):
		'method RegisterFWUpgradeProgressEvent'
		return self._oleobj_.InvokeTypes(29, LCID, 1, (24, 0), (),)

	def SendRebootRequestToCurrentBox(self):
		'method SendRebootRequestToCurrentBox'
		return self._oleobj_.InvokeTypes(45, LCID, 1, (19, 0), (),)

	def SetCurrentDishReceiver(self, receiverID=defaultNamedNotOptArg):
		'method SetCurrentDishReceiver'
		return self._oleobj_.InvokeTypes(44, LCID, 1, (19, 0), ((8, 1),),receiverID
			)

	def Start(self, bForceStart=defaultNamedNotOptArg):
		'This method will connect to current selected slingbox and start streaming'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((3, 1),),bForceStart
			)

	def StartEx(self, bForceStart=defaultNamedNotOptArg, bFastConnect=defaultNamedNotOptArg):
		'This method will connect to current selected slingbox and start streaming'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (24, 0), ((3, 0), (3, 0)),bForceStart
			, bFastConnect)

	def StartStopStreaming(self, bStartStop=defaultNamedNotOptArg, bForceStart=defaultNamedNotOptArg):
		'method StartStopStreaming'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((3, 0), (3, 0)),bStartStop
			, bForceStart)

	def Stop(self):
		'This method will disconnect current slingbox and stop streaming'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AnalyticsSessionId": (37, 2, (8, 0), (), "AnalyticsSessionId", None),
		"ApplicationName": (31, 2, (8, 0), (), "ApplicationName", None),
		# Method 'BoxProps' returns object of type 'IBoxPropsAX'
		"BoxProps": (23, 2, (9, 0), (), "BoxProps", '{DE5F0E99-42D7-4724-AD5F-1B46910B68E1}'),
		"ClientWanIP": (51, 2, (8, 0), (), "ClientWanIP", None),
		# Method 'ClosedCaption' returns object of type 'IClosedCaptionAX'
		"ClosedCaption": (40, 2, (9, 0), (), "ClosedCaption", '{B68271A5-7166-476C-9BE8-D6B9C5372C90}'),
		"ClosedCaptionActivate": (41, 2, (3, 0), (), "ClosedCaptionActivate", None),
		"ConnectionModes": (49, 2, (8, 0), (), "ConnectionModes", None),
		"ConnectionStatus": (19, 2, (2, 0), (), "ConnectionStatus", None),
		# Method 'CurrentBox' returns object of type 'IBoxIdentity'
		"CurrentBox": (3, 2, (9, 0), (), "CurrentBox", '{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}'),
		# Method 'CurrentVideoInput' returns object of type 'IVideoInputAX'
		"CurrentVideoInput": (11, 2, (9, 0), (), "CurrentVideoInput", '{FFA197E7-DBE6-4D19-A9F3-D06FAB3080CC}'),
		# Method 'Devices' returns object of type 'IBoxIdentityEnum'
		"Devices": (4, 2, (9, 0), (), "Devices", '{05FA90E7-297F-4ED9-B041-BCF37C14CB30}'),
		"Environment": (2, 2, (8, 0), (), "Environment", None),
		# Method 'MyMedia' returns object of type 'IMyMedia'
		"MyMedia": (32, 2, (9, 0), (), "MyMedia", '{14D4BE41-CBC6-4030-BA7B-C42CF18BD030}'),
		"PlayerInstanceID": (50, 2, (8, 0), (), "PlayerInstanceID", None),
		# Method 'PlayerProps' returns object of type 'IPlayerPropsAX'
		"PlayerProps": (12, 2, (9, 0), (), "PlayerProps", '{9CEBC8CF-8907-433D-B1D7-41FE2EB1DCDB}'),
		"Position": (33, 2, (3, 0), (), "Position", None),
		# Method 'RemoteControl' returns object of type 'IRemoteControlAX'
		"RemoteControl": (22, 2, (9, 0), (), "RemoteControl", '{626B8C4A-383B-4781-ACC2-D8B661909D43}'),
		"SBSessionId": (36, 2, (19, 0), (), "SBSessionId", None),
		# Method 'SQAParams' returns object of type 'ISQAParamsAX'
		"SQAParams": (24, 2, (9, 0), (), "SQAParams", '{965C70F8-62FE-4732-A338-1B709172B2F9}'),
		# Method 'SUA' returns object of type 'ISUAAX'
		"SUA": (30, 2, (9, 0), (), "SUA", '{DE89D4A9-880F-4536-9F80-CC54CCB93D43}'),
		# Method 'ServiceProxy' returns object of type 'IServiceProxyInfo'
		"ServiceProxy": (34, 2, (9, 0), (), "ServiceProxy", '{B68682A7-55A6-437B-816F-EF7F2587E671}'),
		# Method 'SlingAccounts' returns object of type 'ISlingAccountsAX'
		"SlingAccounts": (28, 2, (9, 0), (), "SlingAccounts", '{5FF8AF7A-B6A3-43AB-9046-8E2D6794B5F0}'),
		"Status": (9, 2, (8, 0), (), "Status", None),
		"StatusCode": (14, 2, (3, 0), (), "StatusCode", None),
		# Method 'StreamSettings' returns object of type 'IStreamSettingsAX'
		"StreamSettings": (15, 2, (9, 0), (), "StreamSettings", '{54B36EA5-5025-4110-9AB6-154090A89024}'),
		# Method 'StreamingProxy' returns object of type 'IStreamingProxyInfo'
		"StreamingProxy": (35, 2, (9, 0), (), "StreamingProxy", '{2896D0D0-04B3-477C-A0A2-4F89FCA8848E}'),
		# Method 'Sunshine' returns object of type 'ISunshine'
		"Sunshine": (39, 2, (9, 0), (), "Sunshine", '{64A1F442-1541-46DF-A87E-96C1C9DB6322}'),
		"Version": (1, 2, (8, 0), (), "Version", None),
		# Method 'VideoInputEnum' returns object of type 'IVideoInputEnum'
		"VideoInputEnum": (10, 2, (9, 0), (), "VideoInputEnum", '{532E3283-36B3-4AA9-91F8-A6EDE9DC4209}'),
	}
	_prop_map_put_ = {
		"ApplicationName": ((31, LCID, 4, 0),()),
		"ClosedCaptionActivate": ((41, LCID, 4, 0),()),
		"ConnectionModes": ((49, LCID, 4, 0),()),
		"EnableACRFeed": ((52, LCID, 4, 0),()),
		"Environment": ((2, LCID, 4, 0),()),
		"Position": ((33, LCID, 4, 0),()),
		"SetPartner": ((26, LCID, 4, 0),()),
		"SetUniqueUserId": ((25, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IStreamSettingsAX(DispatchBaseClass):
	'IStreamSettingsAX Interface'
	CLSID = IID('{54B36EA5-5025-4110-9AB6-154090A89024}')
	coclass_clsid = IID('{84109D64-3E5B-435B-8FA8-99314D1FAA1B}')

	def Apply(self):
		'Apply the changes'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), (),)

	def Cancel(self):
		'Cancel the changes'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def DXVACapability(self):
		'Checks if the system has DXVA capability.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), (),)

	def RestoreToDefaults(self):
		'method RestoreToDefaults'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"AudioBitRate": (10, 2, (18, 0), (), "AudioBitRate", None),
		"EnableDXVA": (15, 2, (3, 0), (), "EnableDXVA", None),
		"FPS": (7, 2, (18, 0), (), "FPS", None),
		"IFrameInterval": (8, 2, (18, 0), (), "IFrameInterval", None),
		"LANVideoRes": (2, 2, (18, 0), (), "LANVideoRes", None),
		"ManualVideoRes": (4, 2, (18, 0), (), "ManualVideoRes", None),
		"RequiredBandWidth": (6, 2, (19, 0), (), "RequiredBandWidth", None),
		"Type": (1, 2, (18, 0), (), "Type", None),
		"VideoBitrate": (5, 2, (18, 0), (), "VideoBitrate", None),
		"VideoRenderer": (16, 2, (3, 0), (), "VideoRenderer", None),
		"VideoSmoothness": (9, 2, (18, 0), (), "VideoSmoothness", None),
		"WANVideoRes": (3, 2, (18, 0), (), "WANVideoRes", None),
	}
	_prop_map_put_ = {
		"AudioBitRate": ((10, LCID, 4, 0),()),
		"EnableDXVA": ((15, LCID, 4, 0),()),
		"FPS": ((7, LCID, 4, 0),()),
		"IFrameInterval": ((8, LCID, 4, 0),()),
		"LANVideoRes": ((2, LCID, 4, 0),()),
		"ManualVideoRes": ((4, LCID, 4, 0),()),
		"Type": ((1, LCID, 4, 0),()),
		"VideoBitrate": ((5, LCID, 4, 0),()),
		"VideoRenderer": ((16, LCID, 4, 0),()),
		"VideoSmoothness": ((9, LCID, 4, 0),()),
		"WANVideoRes": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IStreamingProxyInfo(DispatchBaseClass):
	'IStreamingProxyInfo Interface'
	CLSID = IID('{2896D0D0-04B3-477C-A0A2-4F89FCA8848E}')
	coclass_clsid = IID('{CAF3DA44-9A95-45A7-AC4E-34CA4CC947B6}')

	def Apply(self):
		'method Apply'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Password": (2, 2, (8, 0), (), "Password", None),
		"Port": (4, 2, (3, 0), (), "Port", None),
		"ServerIpAddress": (3, 2, (8, 0), (), "ServerIpAddress", None),
		"UseBrowserProxy": (5, 2, (2, 0), (), "UseBrowserProxy", None),
		"Username": (1, 2, (8, 0), (), "Username", None),
	}
	_prop_map_put_ = {
		"Password": ((2, LCID, 4, 0),()),
		"Port": ((4, LCID, 4, 0),()),
		"ServerIpAddress": ((3, LCID, 4, 0),()),
		"UseBrowserProxy": ((5, LCID, 4, 0),()),
		"Username": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISunshine(DispatchBaseClass):
	'ISunshine Interface'
	CLSID = IID('{64A1F442-1541-46DF-A87E-96C1C9DB6322}')
	coclass_clsid = IID('{4ACD3B99-061D-44A6-B3A0-2E516DADC83D}')

	def ChangeChannel(self, channelNumber=defaultNamedNotOptArg, tvInstance=defaultNamedNotOptArg):
		'method ChangeChannel'
		return self._oleobj_.InvokeTypes(2, LCID, 1, (19, 0), ((19, 1), (19, 1)),channelNumber
			, tvInstance)

	def FireAsyncEventResponse(self, strEventType=defaultNamedNotOptArg, strHTTPMethod=defaultNamedNotOptArg, strHTTPObj=defaultNamedNotOptArg, strPayload=defaultNamedNotOptArg
			, strPassword=defaultNamedNotOptArg, channelNumber=defaultNamedNotOptArg):
		'method FireAsyncEventResponse'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (19, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (19, 1)),strEventType
			, strHTTPMethod, strHTTPObj, strPayload, strPassword, channelNumber
			)

	def FireDVRPlayRequest(self, pvrID=defaultNamedNotOptArg, pvrAttrib=defaultNamedNotOptArg, playMode=defaultNamedNotOptArg):
		'method FireDVRPlayRequest'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (19, 0), ((19, 1), (19, 1), (19, 1)),pvrID
			, pvrAttrib, playMode)

	def FireJoinTunerRequest(self, tunerIndex=defaultNamedNotOptArg, svcId=defaultNamedNotOptArg, connId=defaultNamedNotOptArg):
		'method FireJoinTunerRequest'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (19, 0), ((19, 1), (19, 1), (19, 1)),tunerIndex
			, svcId, connId)

	def FireLandingPageRequest(self):
		'method FireLandingPageRequest'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (19, 0), (),)

	def FireRebootRequest(self):
		'method FireRebootRequest'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (19, 0), (),)

	def GetTVInfo(self, bWakeUP=defaultNamedNotOptArg):
		'method GetTVInfo'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (19, 0), ((19, 1),),bWakeUP
			)

	def IsBoxSunshineCapable(self):
		'method IsBoxSunshineCapable'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (19, 0), (),)

	def IsCapable(self, featureId=defaultNamedNotOptArg):
		'method IsCapable'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (19, 0), ((19, 1),),featureId
			)

	def Login(self, reciverId=defaultNamedNotOptArg, cookie=defaultNamedNotOptArg):
		'method Login'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (19, 0), ((8, 1), (8, 1)),reciverId
			, cookie)

	def SetAsyncEventsSubscription(self, subscribeAE=defaultNamedNotOptArg):
		'method SetAsyncEventsSubscription'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (19, 0), ((19, 1),),subscribeAE
			)

	def SetBufferBarEventsSubscription(self, subscribeBB=defaultNamedNotOptArg):
		'method SetBufferBarEventsSubscription'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (19, 0), ((19, 1),),subscribeBB
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVideoInputAX(DispatchBaseClass):
	'IVideoInputAX Interface'
	CLSID = IID('{FFA197E7-DBE6-4D19-A9F3-D06FAB3080CC}')
	coclass_clsid = IID('{608295BB-C114-4569-9305-FE7A6792D5FC}')

	def DownloadRemoteControl(self):
		'method DownloadRemoteControl'
		return self._oleobj_.InvokeTypes(37, LCID, 1, (24, 0), (),)

	# Result is of type IChannel
	def GetChannelAt(self, ulIndex=defaultNamedNotOptArg):
		'Get the channel information based on the specified index.'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((19, 1),),ulIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetChannelAt', '{4192D38F-9410-41EF-AAE0-9F850B1A689F}')
		return ret

	def HDMI_RefreshStatus(self):
		'method HDMI_RefreshStatus'
		return self._oleobj_.InvokeTypes(35, LCID, 1, (24, 0), (),)

	def LoadInputConfig(self):
		'method LoadInputConfig'
		return self._oleobj_.InvokeTypes(36, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"ChannelsCount": (10, 2, (19, 0), (), "ChannelsCount", None),
		"Country": (16, 2, (19, 0), (), "Country", None),
		"CurrentChannel": (24, 2, (8, 0), (), "CurrentChannel", None),
		"DeviceBrand": (17, 2, (8, 0), (), "DeviceBrand", None),
		"DeviceIRCode": (19, 2, (8, 0), (), "DeviceIRCode", None),
		"DeviceModel": (18, 2, (8, 0), (), "DeviceModel", None),
		"DeviceType": (14, 2, (19, 0), (), "DeviceType", None),
		"HDMI_HDCPStatus": (31, 2, (3, 0), (), "HDMI_HDCPStatus", None),
		"HDMI_OnPlaceShiftingDisabledAssociatedInput": (34, 2, (3, 0), (), "HDMI_OnPlaceShiftingDisabledAssociatedInput", None),
		"HDMI_OnPlaceShiftingDisabledReason": (33, 2, (3, 0), (), "HDMI_OnPlaceShiftingDisabledReason", None),
		"HDMI_OnPlaceShiftingStatus": (32, 2, (3, 0), (), "HDMI_OnPlaceShiftingStatus", None),
		"HDMI_PhysicalPortStatus": (28, 2, (3, 0), (), "HDMI_PhysicalPortStatus", None),
		"HDMI_SoftDisabledReason": (30, 2, (3, 0), (), "HDMI_SoftDisabledReason", None),
		"HDMI_SoftStatus": (29, 2, (3, 0), (), "HDMI_SoftStatus", None),
		"ID": (2, 2, (19, 0), (), "ID", None),
		"IRDigits": (20, 2, (19, 0), (), "IRDigits", None),
		"IRKeyCodes": (23, 2, (8, 0), (), "IRKeyCodes", None),
		"IRKeyDelay": (25, 2, (19, 0), (), "IRKeyDelay", None),
		"IRKeysCount": (22, 2, (19, 0), (), "IRKeysCount", None),
		"IsAutoAspectSupported": (8, 2, (3, 0), (), "IsAutoAspectSupported", None),
		"IsConfigurable": (26, 2, (19, 0), (), "IsConfigurable", None),
		"IsCurrent": (6, 2, (3, 0), (), "IsCurrent", None),
		"IsEPGSupported": (7, 2, (3, 0), (), "IsEPGSupported", None),
		"IsTuner": (5, 2, (3, 0), (), "IsTuner", None),
		"Lineup": (1, 2, (8, 0), (), "Lineup", None),
		"Lineup2": (12, 2, (8, 0), (), "Lineup2", None),
		"Name": (3, 2, (8, 0), (), "Name", None),
		"Type": (9, 2, (19, 0), (), "Type", None),
		"VideoLock": (27, 2, (3, 0), (), "VideoLock", None),
		"VideoStandard": (15, 2, (8, 0), (), "VideoStandard", None),
		"WantsEnter": (21, 2, (19, 0), (), "WantsEnter", None),
		"Zipcode": (4, 2, (19, 0), (), "Zipcode", None),
		"Zipcode2": (13, 2, (8, 0), (), "Zipcode2", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVideoInputEnum(DispatchBaseClass):
	'IVideoInputEnum Interface'
	CLSID = IID('{532E3283-36B3-4AA9-91F8-A6EDE9DC4209}')
	coclass_clsid = IID('{97C4E939-FD29-4D6D-8C5F-65C99A72D128}')

	# Result is of type IVideoInputAX
	# The method At is actually a property, but must be used as a method to correctly pass the arguments
	def At(self, ulIndex=defaultNamedNotOptArg):
		'property At'
		ret = self._oleobj_.InvokeTypes(2, LCID, 2, (9, 0), ((19, 1),),ulIndex
			)
		if ret is not None:
			ret = Dispatch(ret, 'At', '{FFA197E7-DBE6-4D19-A9F3-D06FAB3080CC}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (19, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (19, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class _ISlingPlayerEvents:
	'_ISlingPlayerEvents Interface'
	CLSID = CLSID_Sink = IID('{F68B3100-BDA6-42FF-A765-BC6EC5415FA7}')
	coclass_clsid = IID('{B80CD4E6-5B02-4B6C-99BE-68F1511E9549}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        1 : "OnonControlInitialise",
		        2 : "OnDiscoveryComplete",
		        3 : "OnStatusChange",
		        4 : "OnonStartComplete",
		        5 : "OnonInputChange",
		        6 : "OnonPlayerError",
		        7 : "OnonBufferStatus",
		        8 : "OnonSlingAccounts",
		        9 : "OnonAspectRatioChange",
		       10 : "OnonRemoteControlStatusChange",
		       11 : "OnonSUAEvent",
		       12 : "OnonConnectionModeChange",
		       13 : "OnChannelInfoLoad",
		       14 : "OnonRemoteControlKeyPress",
		       15 : "OnonServiceInitialise",
		       16 : "OnonRemoteControlDownloadStatus",
		       17 : "OnonChannelChange",
		       18 : "OnFWUpgradeEvent",
		       20 : "OnHDMI_StatusChange",
		       21 : "OnSQAMonitoringStatusChange",
		       22 : "OnHDMI_RefreshComplete",
		       23 : "OnMyMedia",
		       24 : "OnTSBResume",
		       25 : "OnSunshineChannelChangeCompletion",
		       26 : "OnSunshineEvent",
		       27 : "OnRebootRequestHandlingCompletion",
		       28 : "OnRemoteControlDownloadComplete",
		       29 : "OnLoadInputConfigComplete",
		       30 : "OnLoadDeviceConfigComplete",
		       31 : "OnSparcsResponse",
		       32 : "OnUserInputEvent",
		       33 : "OnAcrInit",
		       34 : "OnACRResponse",
		       35 : "OnACRBindUser",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnonControlInitialise(self):
#		'This method will be called after the control is initialised and ready for operation.'
#	def OnDiscoveryComplete(self, pEnum=defaultNamedNotOptArg):
#		'method OnDiscoveryComplete'
#	def OnStatusChange(self):
#		'method OnStatusChange'
#	def OnonStartComplete(self):
#		'method onStartComplete'
#	def OnonInputChange(self):
#		'method onInputChange'
#	def OnonPlayerError(self, nCode=defaultNamedNotOptArg):
#		'method onPlayerError'
#	def OnonBufferStatus(self, nPos=defaultNamedNotOptArg, nMin=defaultNamedNotOptArg, nMax=defaultNamedNotOptArg):
#		'method onBufferStatus'
#	def OnonSlingAccounts(self, wParam=defaultNamedNotOptArg, lParam=defaultNamedNotOptArg):
#		'All SlingAccounts operations are completed by this method'
#	def OnonAspectRatioChange(self):
#		'This method will get called when aspect ratio will change'
#	def OnonRemoteControlStatusChange(self):
#		'This method will be fired whenever remote control availability status is changed'
#	def OnonSUAEvent(self, nStateId=defaultNamedNotOptArg, nMethodId=defaultNamedNotOptArg, nPropId=defaultNamedNotOptArg, nEventStatus=defaultNamedNotOptArg
#			, nAdditionalInfo=defaultNamedNotOptArg):
#		'method onSUAEvent'
#	def OnonConnectionModeChange(self, nMode=defaultNamedNotOptArg):
#		'method onConnectionModeChange'
#	def OnChannelInfoLoad(self):
#		'Event will be fired when channel info is loaded for tuner input'
#	def OnonRemoteControlKeyPress(self, wszKeyCmd=defaultNamedNotOptArg, nKeyCode=defaultNamedNotOptArg):
#		'method onRemoteControlKeyPress'
#	def OnonServiceInitialise(self):
#		'method onServiceInitialise'
#	def OnonRemoteControlDownloadStatus(self, Status=defaultNamedNotOptArg):
#		'Event will be fired when a remote control is downloaded.'
#	def OnonChannelChange(self):
#		'method onChannelChange'
#	def OnFWUpgradeEvent(self, iEvent=defaultNamedNotOptArg, iAddinfo1=defaultNamedNotOptArg, iAddinfo2=defaultNamedNotOptArg):
#		'This method will be fired when FWUpgrade event occurs'
#	def OnHDMI_StatusChange(self):
#		'method OnHDMI_StatusChange'
#	def OnSQAMonitoringStatusChange(self, Status=defaultNamedNotOptArg):
#		'method OnSQAMonitoringStatusChange.This method will be fired when SQA starts or stops'
#	def OnHDMI_RefreshComplete(self, adwEventCode=defaultNamedNotOptArg):
#		'method OnHDMIRefreshComplete'
#	def OnMyMedia(self, nMMCmd=defaultNamedNotOptArg, nMMCmdStatus=defaultNamedNotOptArg, szData=defaultNamedNotOptArg):
#		'OnMyMedia event for various MM events'
#	def OnTSBResume(self):
#		'OnTSBResume event for  TSB auto resume'
#	def OnSunshineChannelChangeCompletion(self, nStatus=defaultNamedNotOptArg):
#		'method OnSunshineChannelChangeCompletion'
#	def OnSunshineEvent(self, eventID=defaultNamedNotOptArg, eventStatus=defaultNamedNotOptArg, extraJsonData=defaultNamedNotOptArg):
#		'method OnSunshineEvent'
#	def OnRebootRequestHandlingCompletion(self, nStatus=defaultNamedNotOptArg):
#		'method OnRebootRequestHandlingCompletion'
#	def OnRemoteControlDownloadComplete(self, nStatus=defaultNamedNotOptArg):
#		'method OnRemoteControlDownloadComplete'
#	def OnLoadInputConfigComplete(self, nStatus=defaultNamedNotOptArg):
#		'method OnLoadInputConfigComplete'
#	def OnLoadDeviceConfigComplete(self, nStatus=defaultNamedNotOptArg):
#		'method OnLoadDeviceConfigComplete'
#	def OnSparcsResponse(self, nStatus=defaultNamedNotOptArg, szResponse=defaultNamedNotOptArg):
#		'method OnSparcsResponse'
#	def OnUserInputEvent(self, iEventType=defaultNamedNotOptArg, iAddinfo1=defaultNamedNotOptArg, iAddinfo2=defaultNamedNotOptArg):
#		'method OnUserInputEvent'
#	def OnAcrInit(self, nStatus=defaultNamedNotOptArg):
#		'method OnAcrInit'
#	def OnACRResponse(self, bstrBrand=defaultNamedNotOptArg, bstrNetWork=defaultNamedNotOptArg, udwChannelNumber=defaultNamedNotOptArg, bstrTitle=defaultNamedNotOptArg
#			, bstrTMSInfo=defaultNamedNotOptArg, bstrType=defaultNamedNotOptArg, bstrTimeStamp=defaultNamedNotOptArg):
#		'method OnACRResponse'
#	def OnACRBindUser(self, nStatus=defaultNamedNotOptArg, bstrUserId=defaultNamedNotOptArg):
#		'method OnACRBindUser'


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'SlingPlayerAX.BoxIdentity.1'
class BoxIdentity(CoClassBaseClass): # A CoClass
	# BoxIdentity Class
	CLSID = IID('{00774808-0A96-45CA-A55B-B608BEE33B6E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBoxIdentity,
	]
	default_interface = IBoxIdentity

# This CoClass is known by the name 'SlingPlayerAX.BoxIdentityEnum.1'
class BoxIdentityEnum(CoClassBaseClass): # A CoClass
	# BoxIdentityEnum Class
	CLSID = IID('{EFBEECAF-71BD-4D66-A184-51B9F5252698}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBoxIdentityEnum,
	]
	default_interface = IBoxIdentityEnum

# This CoClass is known by the name 'SlingPlayerAX.BoxPropsAX.1'
class BoxPropsAX(CoClassBaseClass): # A CoClass
	# BoxPropsAX Class
	CLSID = IID('{DE947688-953F-4122-A9AE-1365AE038FED}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IBoxPropsAX,
	]
	default_interface = IBoxPropsAX

# This CoClass is known by the name 'SlingPlayerAX.Channel.1'
class Channel(CoClassBaseClass): # A CoClass
	# Channel Class
	CLSID = IID('{59E91392-CAD0-4DB9-84A8-4A57C6AFDF1E}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IChannel,
	]
	default_interface = IChannel

# This CoClass is known by the name 'SlingPlayerAX.ClosedCaptionAX.1'
class ClosedCaptionAX(CoClassBaseClass): # A CoClass
	# ClosedCaptionAX Class
	CLSID = IID('{16E1B18E-55D9-4191-8C83-F0404CE38443}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IClosedCaptionAX,
	]
	default_interface = IClosedCaptionAX

# This CoClass is known by the name 'SlingPlayerAX.MyMedia.1'
class MyMedia(CoClassBaseClass): # A CoClass
	# MyMedia Class
	CLSID = IID('{9B3E9F8A-72A6-4B41-9432-1B0F8D1EDD2B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IMyMedia,
	]
	default_interface = IMyMedia

# This CoClass is known by the name 'SlingPlayerAX.PlayerPropsAX.1'
class PlayerPropsAX(CoClassBaseClass): # A CoClass
	# PlayerPropsAX Class
	CLSID = IID('{3B2CBA5C-8D99-4A1D-A834-6E1543784FE4}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IPlayerPropsAX,
	]
	default_interface = IPlayerPropsAX

# This CoClass is known by the name 'SlingPlayerAX.RemoteControlAX.1'
class RemoteControlAX(CoClassBaseClass): # A CoClass
	# RemoteControlAX Class
	CLSID = IID('{DCEA4309-3D50-4991-AA21-18BE5A9571C6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRemoteControlAX,
	]
	default_interface = IRemoteControlAX

# This CoClass is known by the name 'SlingPlayerAX.SQAParamsAX.1'
class SQAParamsAX(CoClassBaseClass): # A CoClass
	# SQAParamsAX Class
	CLSID = IID('{C95D46F1-30C7-4889-AFB8-1FF19A207AF5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISQAParamsAX,
	]
	default_interface = ISQAParamsAX

# This CoClass is known by the name 'SlingPlayerAX.SUAAX.1'
class SUAAX(CoClassBaseClass): # A CoClass
	# SUAAX Class
	CLSID = IID('{D79B47D1-384C-4D00-B7A3-023D4F9655B3}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISUAAX,
	]
	default_interface = ISUAAX

# This CoClass is known by the name 'SlingPlayerAX.ServiceProxyInfo.1'
class ServiceProxyInfo(CoClassBaseClass): # A CoClass
	# ServiceProxyInfo Class
	CLSID = IID('{F4853AF6-146C-4D56-A60D-83767F565F87}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IServiceProxyInfo,
	]
	default_interface = IServiceProxyInfo

# This CoClass is known by the name 'SlingPlayerAX.SlingAccountsAX.1'
class SlingAccountsAX(CoClassBaseClass): # A CoClass
	# SlingAccountsAX Class
	CLSID = IID('{B8085032-9FDE-43DE-8683-C6FE8379CAE5}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISlingAccountsAX,
	]
	default_interface = ISlingAccountsAX

# This CoClass is known by the name 'SlingPlayerAX.SlingPlayer.1'
class SlingPlayer(CoClassBaseClass): # A CoClass
	# SlingPlayer Class
	CLSID = IID('{B80CD4E6-5B02-4B6C-99BE-68F1511E9549}')
	coclass_sources = [
		_ISlingPlayerEvents,
	]
	default_source = _ISlingPlayerEvents
	coclass_interfaces = [
		ISlingPlayer,
	]
	default_interface = ISlingPlayer

# This CoClass is known by the name 'SlingPlayerAX.StreamSettingsAX.1'
class StreamSettingsAX(CoClassBaseClass): # A CoClass
	# StreamSettingsAX Class
	CLSID = IID('{84109D64-3E5B-435B-8FA8-99314D1FAA1B}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IStreamSettingsAX,
	]
	default_interface = IStreamSettingsAX

# This CoClass is known by the name 'SlingPlayerAX.StreamingProxyInfo.1'
class StreamingProxyInfo(CoClassBaseClass): # A CoClass
	# StreamingProxyInfo Class
	CLSID = IID('{CAF3DA44-9A95-45A7-AC4E-34CA4CC947B6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IStreamingProxyInfo,
	]
	default_interface = IStreamingProxyInfo

# This CoClass is known by the name 'SlingPlayerAX.Sunshine.1'
class Sunshine(CoClassBaseClass): # A CoClass
	# Sunshine Class
	CLSID = IID('{4ACD3B99-061D-44A6-B3A0-2E516DADC83D}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISunshine,
	]
	default_interface = ISunshine

# This CoClass is known by the name 'SlingPlayerAX.VideoInputAX.1'
class VideoInputAX(CoClassBaseClass): # A CoClass
	# VideoInputAX Class
	CLSID = IID('{608295BB-C114-4569-9305-FE7A6792D5FC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVideoInputAX,
	]
	default_interface = IVideoInputAX

# This CoClass is known by the name 'SlingPlayerAX.VideoInputEnum.1'
class VideoInputEnum(CoClassBaseClass): # A CoClass
	# VideoInputEnum Class
	CLSID = IID('{97C4E939-FD29-4D6D-8C5F-65C99A72D128}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IVideoInputEnum,
	]
	default_interface = IVideoInputEnum

IBoxIdentity_vtables_dispatch_ = 1
IBoxIdentity_vtables_ = [
	(( 'FinderID' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FinderID' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IPAddress' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IPAddress' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Port' , 'pVal' , ), 3, (3, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Port' , 'pVal' , ), 3, (3, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseIPPort' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseIPPort' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Username' , 'pVal' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Username' , 'pVal' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'pVal' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ProductID' , 'pVal' , ), 7, (7, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Initialised' , 'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
	(( 'GetPassword' , 'pVal' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 64 , )),
	(( 'Assign' , 'pBox' , ), 10, (10, (), [ (9, 1, None, "IID('{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 64 , )),
	(( 'SetProductID' , 'nProductID' , ), 11, (11, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 64 , )),
	(( 'Name' , 'pVal' , ), 12, (12, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SetName' , 'sDevName' , ), 13, (13, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( 'IsSaved' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'IsDiscovered' , 'pVal' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'IsConfigured' , 'pVal' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IsAvailable' , 'pVal' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DiscoveryState' , 'pVal' , ), 18, (18, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 64 , )),
	(( 'Save' , 'pVal' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Save' , 'pVal' , ), 19, (19, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionString' , 'pVal' , ), 20, (20, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionString' , 'pVal' , ), 20, (20, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'LoadDeviceConfig' , ), 21, (21, (), [ ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IBoxIdentityEnum_vtables_dispatch_ = 1
IBoxIdentityEnum_vtables_ = [
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'At' , 'ulIndex' , 'pVal' , ), 2, (2, (), [ (19, 1, None, None) , 
			 (16393, 10, None, "IID('{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FinderID' , 'strFinderId' , 'pVal' , ), 3, (3, (), [ (8, 0, None, None) , 
			 (16393, 10, None, "IID('{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'pVal' , ), 4, (4, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IBoxPropsAX_vtables_dispatch_ = 1
IBoxPropsAX_vtables_ = [
	(( 'MAC' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ProductID' , 'pVal' , ), 3, (3, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'HardwareVersion' , 'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IRBlasterVersion' , 'pVal' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FirmwareVersion' , 'pVal' , ), 6, (6, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FirmwareReleaseDate' , 'pVal' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'IPType' , 'pVal' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'IPAddress' , 'pVal' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'IPSubnetMask' , 'pVal' , ), 10, (10, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GatewayIP' , 'pVal' , ), 11, (11, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Port' , 'pVal' , ), 12, (12, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LastConflictedIP' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UPNPIGDRouterIP' , 'pVal' , ), 14, (14, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UPNPIGDRouterPort' , 'pVal' , ), 15, (15, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UPNPURI' , 'pVal' , ), 16, (16, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'WANAccess' , 'pVal' , ), 17, (17, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'RemoteConfiguration' , 'pVal' , ), 18, (18, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SlingServerIP' , 'pVal' , ), 19, (19, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SlingServerPort' , 'pVal' , ), 20, (20, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'IsRegistered' , 'pVal' , ), 21, (21, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RegistrationPeriod' , 'pVal' , ), 22, (22, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Ping' , 'pVal' , ), 23, (23, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'PingPeriod' , 'pVal' , ), 24, (24, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MSGServer' , 'pVal' , ), 25, (25, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'MSGServerPorts' , 'pVal' , ), 26, (26, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Country' , 'pVal' , ), 27, (27, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'LastUpdated' , 'pVal' , ), 28, (28, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DefaultCountryCode' , 'pVal' , ), 29, (29, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'IsLocal' , 'pVal' , ), 30, (30, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'HWMajorVersion' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'HWMinorVersion' , 'pVal' , ), 32, (32, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'HWBuildVersion' , 'pVal' , ), 33, (33, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CheckLebowskiSupported' , 'sLeboType' , 'pVal' , ), 34, (34, (), [ (18, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionSessionID' , 'pVal' , ), 35, (35, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'IsConfigured' , 'pVal' , ), 36, (36, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'CountryCode' , 'pVal' , ), 37, (37, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'IsCapable' , 'capability' , 'pVal' , ), 38, (38, (), [ (3, 0, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'LastInputIndex' , 'pVal' , ), 39, (39, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'DestinationIP' , 'pVal' , ), 40, (40, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'DestinationPort' , 'pVal' , ), 41, (41, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RelayManagerStartUrl' , 'pVal' , ), 42, (42, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'RelayManagerEndUrl' , 'pVal' , ), 43, (43, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'DeviceIPAddress' , 'pVal' , ), 44, (44, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
]

IChannel_vtables_dispatch_ = 1
IChannel_vtables_ = [
	(( 'MajorChannelNo' , 'pVal' , ), 1, (1, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MinorChannelNo' , 'pVal' , ), 2, (2, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Frequency' , 'pVal' , ), 3, (3, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ChannelAsString' , 'pVal' , ), 4, (4, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IClosedCaptionAX_vtables_dispatch_ = 1
IClosedCaptionAX_vtables_ = [
	(( 'Visible' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FontColor' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FontColor' , 'pVal' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FontSize' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FontSize' , 'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FontStyle' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FontStyle' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'FontEdgeStyle' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FontEdgeStyle' , 'pVal' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FontEdgeColor' , 'pVal' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'FontEdgeColor' , 'pVal' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FontOpacity' , 'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FontOpacity' , 'pVal' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'BGColor' , 'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'BGColor' , 'pVal' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BGOpacity' , 'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BGOpacity' , 'pVal' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SetServiceChannel' , 'nChannel' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SetCCDefaults' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'WindowColor' , 'pVal' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'WindowColor' , 'pVal' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IMyMedia_vtables_dispatch_ = 1
IMyMedia_vtables_ = [
	(( 'Start' , 'playURL' , 'offset' , ), 1, (1, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Seek' , 'offset' , 'Flush' , ), 2, (2, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Pause' , 'Flush' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Resume' , 'offset' , 'Flush' , ), 4, (4, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Stop' , 'bookmark' , 'Flush' , ), 5, (5, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ChangeContent' , 'playURL' , 'offset' , 'Flush' , ), 6, (6, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IPlayerPropsAX_vtables_dispatch_ = 1
IPlayerPropsAX_vtables_ = [
	(( 'AspectRatio' , 'pVal' , ), 1, (1, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AspectRatio' , 'pVal' , ), 1, (1, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Volume' , 'pVal' , ), 2, (2, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Volume' , 'pVal' , ), 2, (2, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShowClosedCaption' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ShowClosedCaption' , 'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Bitrate' , 'pVal' , ), 4, (4, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RenderFramerate' , 'pVal' , ), 5, (5, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'BufferLength' , 'pVal' , ), 6, (6, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'BufferLength' , 'pVal' , ), 6, (6, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Mute' , 'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Mute' , 'pVal' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FullScreen' , 'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FullScreen' , 'pVal' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'BufferStatusUpdateInterval' , 'pVal' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'BufferStatusUpdateInterval' , 'pVal' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ActualVideoWidth' , 'pVal' , ), 10, (10, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActualVideoHeight' , 'pVal' , ), 11, (11, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CropBorder' , 'pVal' , ), 12, (12, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CropBorder' , 'pVal' , ), 12, (12, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ShowStatisticsWindow' , 'bShow' , ), 13, (13, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'IsStatisticsWindowVisible' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CurrentFirmwareVersion' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'LatestFirmwareVersion' , 'pVal' , ), 16, (16, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'IsFirmwareUpdateRequired' , 'bUpdateReqired' , ), 17, (17, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ShowBoxInfoWindow' , 'bShow' , ), 18, (18, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'IsBoxInfoWindowVisible' , 'pVal' , ), 19, (19, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'VideoBitrate' , 'pVal' , ), 20, (20, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'AudioBitRate' , 'pVal' , ), 21, (21, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'IFrameInterval' , 'pVal' , ), 22, (22, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'StreamFramerate' , 'pVal' , ), 23, (23, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'StreamVideoWidth' , 'pVal' , ), 24, (24, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'StreamVideoHeight' , 'pVal' , ), 25, (25, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'PresentationTime' , 'pVal' , ), 26, (26, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'VideoCodecType' , 'pVal' , ), 27, (27, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'AudioCodecType' , 'pVal' , ), 28, (28, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'StreamType' , 'pVal' , ), 29, (29, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'DeviceConnectionCaps' , 'pVal' , ), 30, (30, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'FramesSkipped' , 'pVal' , ), 31, (31, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'VideoRenderType' , 'pVal' , ), 32, (32, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'Precharge' , 'pVal' , ), 33, (33, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'PlaySpeed' , 'pVal' , ), 34, (34, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'OutputAspectRatio' , 'pVal' , ), 35, (35, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseInbandUI' , 'pVal' , ), 36, (36, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseInbandUI' , 'pVal' , ), 36, (36, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'DisableIR' , ), 37, (37, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'ProbeDXVAFromHint' , 'bstrXmlContent' , ), 38, (38, (), [ (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'RemainingStreamTime' , 'pVal' , ), 39, (39, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'ExtendedStreamTime' , ), 40, (40, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'GetFileLocation' , 'iFileType' , 'bstrXmlContent' , ), 41, (41, (), [ (18, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'AudioOnly' , 'pVal' , ), 43, (43, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'AudioOnly' , 'pVal' , ), 43, (43, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'AudioType' , 'pVal' , ), 44, (44, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'AudioType' , 'pVal' , ), 44, (44, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Flush' , 'bFlushBox' , ), 45, (45, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'IsClosedCaptionSupported' , 'pVal' , ), 46, (46, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'VideoRenderTypeNum' , 'pVal' , ), 47, (47, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'RemoteControlPosition' , 'pVal' , ), 48, (48, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'RemoteControlPosition' , 'pVal' , ), 48, (48, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'FloatingWindow' , 'pVal' , ), 49, (49, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'FloatingWindow' , 'pVal' , ), 49, (49, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'DisplayState' , 'pVal' , ), 50, (50, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'IsfastHDSwitchingSupported' , 'pVal' , ), 51, (51, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'SPARCSURL' , 'bstrSPARCSURL' , ), 52, (52, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'KeyFrameAspectRatio' , 'pVal' , ), 53, (53, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ToggleTSB' , 'pVal' , ), 54, (54, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'ToggleTSB' , 'pVal' , ), 54, (54, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'ToggleNativeInputHandling' , ), 55, (55, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'SetFocusToVideoWindow' , ), 56, (56, (), [ ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
]

IRemoteControlAX_vtables_dispatch_ = 1
IRemoteControlAX_vtables_ = [
	(( 'Show' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IsAvailable' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RemoteServicesURL' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetRemoteCount' , 'pVal' , ), 4, (4, (), [ (16401, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Current' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ChannelUp' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ChannelDown' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ChannelLast' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SendCommand' , 'lCode' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SetChannel' , 'szChannel' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GetRemoteByIndex' , 'byIndex' , 'strRemotename' , ), 11, (11, (), [ (3, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SelectRemote' , 'ulIndex' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'RemoteGUID' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'PositionRemote' , 'left' , 'top' , ), 15, (15, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ToggleMove' , 'bEnable' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'NotiyUserInput' , 'bEnable' , ), 17, (17, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

ISQAParamsAX_vtables_dispatch_ = 1
ISQAParamsAX_vtables_ = [
	(( 'LogBadVideo' , ), 1, (1, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'NetworkHealthIndex' , 'pVal' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PlaybackHealthIndex' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PrechargeIndex' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'BitrateIndex' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SystemCapsIndex' , 'pVal' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SQAEnabledCheck' , 'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISUAAX_vtables_dispatch_ = 1
ISUAAX_vtables_ = [
	(( 'GetProperty' , 'nPropId' , 'outData' , ), 1, (1, (), [ (3, 0, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SetProperty' , 'nPropId' , 'inData' , 'nWaitForEvent' , ), 2, (2, (), [ 
			 (3, 0, None, None) , (12, 0, None, None) , (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Start' , 'nState' , ), 3, (3, (), [ (2, 0, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'End' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MoveToState' , 'nState' , ), 5, (5, (), [ (2, 0, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Apply' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Cancel' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Scan' , 'nDetailedScan' , ), 8, (8, (), [ (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UploadIRBinFile' , 'fileName' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ChangeChannel' , 'Channel' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SendIRKey' , 'nIRKey' , ), 11, (11, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SetConfigStatus' , 'bSuccess' , ), 12, (12, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'IsModified' , 'modified' , ), 13, (13, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FirmwareUpload' , 'fileName' , 'bRestartAfterUpdate' , ), 14, (14, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetChannelAt' , 'ulIndex' , 'ptrChannelInfo' , ), 15, (15, (), [ (19, 1, None, None) , 
			 (16393, 10, None, "IID('{4192D38F-9410-41EF-AAE0-9F850B1A689F}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'RVStartAutomaticConfiguration' , ), 16, (16, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'RVStartManualConfiguration' , ), 17, (17, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'RestoreDefaultPictureSettings' , ), 18, (18, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'InitPossibleDeviceTypes' , 'CountryInfo' , ), 19, (19, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetPossibleDeviceInfo' , 'ulIndex' , 'nDeviceType' , ), 20, (20, (), [ (19, 1, None, None) , 
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RVSkip' , ), 21, (21, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RVDisable' , ), 22, (22, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UpdateLatestFirmwareFromServer' , 'bRestartAfterUpdate' , ), 23, (23, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AutoUploadIRBinFile' , 'strURLName' , ), 24, (24, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetLatestRemotes' , ), 25, (25, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CurrentState' , 'pVal' , ), 26, (26, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'LoadKeyMap' , ), 28, (28, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CompareCredentials' , 'nIndex' , 'inStrData' , 'bIsEqual' , ), 29, (29, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'PsessionID' , 'pVal' , ), 30, (30, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'PsessionID' , 'pVal' , ), 30, (30, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SetZipcode' , 'Zipcode' , ), 31, (31, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ResetInput' , 'ulInputIndex' , ), 32, (32, (), [ (19, 0, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ControlInternalIRBlast' , 'bEnableInternal' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ScanInputVideoLock' , 'uTimeoutMsec' , 'nInputMask' , ), 34, (34, (), [ (19, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_SoftControlHDMI' , 'lEnableHDMI' , ), 35, (35, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_ControlHDCP' , 'lEnableHDCP' , ), 36, (36, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_DisableHDMIOnPlaceShifting' , 'lDisableReason' , 'lAssociatedInputIndex' , ), 37, (37, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_ResetDisableHDMIOnPlaceShifting' , ), 38, (38, (), [ ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'StartNGSBConnfig' , 'bTakeOver' , 'nSUAState' , ), 39, (39, (), [ (3, 1, None, None) , 
			 (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IServiceProxyInfo_vtables_dispatch_ = 1
IServiceProxyInfo_vtables_ = [
	(( 'Username' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Username' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseBrowserProxy' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseBrowserProxy' , 'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Apply' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISlingAccountsAX_vtables_dispatch_ = 1
ISlingAccountsAX_vtables_ = [
	(( 'TicketID' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MemberID' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'URL' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Initialize' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AddorEditBox' , 'strFinder' , 'strDevName' , 'strUserName' , 'strPassword' , 
			 ), 5, (5, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RemoveBox' , 'strFinder' , ), 6, (6, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AddEditBoxUsingIpPort' , 'strIpAddress' , 'lPort' , 'strDisplayName' , 'strUserName' , 
			 'strPassword' , 'bUseIpPort' , ), 7, (7, (), [ (8, 1, None, None) , (3, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RemoveBoxUsingIpPort' , 'strIpAddress' , 'lPort' , ), 8, (8, (), [ (8, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISlingPlayer_vtables_dispatch_ = 1
ISlingPlayer_vtables_ = [
	(( 'Version' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Environment' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Environment' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CurrentBox' , 'pVal' , ), 3, (3, (), [ (16393, 10, None, "IID('{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Devices' , 'pVal' , ), 4, (4, (), [ (16393, 10, None, "IID('{05FA90E7-297F-4ED9-B041-BCF37C14CB30}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Discover' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 2 , )),
	(( 'Start' , 'bForceStart' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Stop' , ), 7, (7, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , ), 8, (8, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Status' , 'pVal' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'VideoInputEnum' , 'pVal' , ), 10, (10, (), [ (16393, 10, None, "IID('{532E3283-36B3-4AA9-91F8-A6EDE9DC4209}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'CurrentVideoInput' , 'pVal' , ), 11, (11, (), [ (16393, 10, None, "IID('{FFA197E7-DBE6-4D19-A9F3-D06FAB3080CC}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PlayerProps' , 'pVal' , ), 12, (12, (), [ (16393, 10, None, "IID('{9CEBC8CF-8907-433D-B1D7-41FE2EB1DCDB}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ChangeVideoInput' , 'ulInputIndex' , ), 13, (13, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'StatusCode' , 'pVal' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'StreamSettings' , 'pVal' , ), 15, (15, (), [ (16393, 10, None, "IID('{54B36EA5-5025-4110-9AB6-154090A89024}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Play' , ), 16, (16, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Pause' , ), 17, (17, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'StartStopStreaming' , 'bStartStop' , 'bForceStart' , ), 18, (18, (), [ (3, 0, None, None) , 
			 (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionStatus' , 'pVal' , ), 19, (19, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'StartEx' , 'bForceStart' , 'bFastConnect' , ), 20, (20, (), [ (3, 0, None, None) , 
			 (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ConnectEx' , 'bFastConnect' , ), 21, (21, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RemoteControl' , 'pVal' , ), 22, (22, (), [ (16393, 10, None, "IID('{626B8C4A-383B-4781-ACC2-D8B661909D43}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BoxProps' , 'pVal' , ), 23, (23, (), [ (16393, 10, None, "IID('{DE5F0E99-42D7-4724-AD5F-1B46910B68E1}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SQAParams' , 'pVal' , ), 24, (24, (), [ (16393, 10, None, "IID('{965C70F8-62FE-4732-A338-1B709172B2F9}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'SetUniqueUserId' , ), 25, (25, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'SetPartner' , ), 26, (26, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FeatureSupport' , 'nFeature' , 'bSupport' , ), 27, (27, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'SlingAccounts' , 'pVal' , ), 28, (28, (), [ (16393, 10, None, "IID('{5FF8AF7A-B6A3-43AB-9046-8E2D6794B5F0}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'RegisterFWUpgradeProgressEvent' , ), 29, (29, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SUA' , 'pVal' , ), 30, (30, (), [ (16393, 10, None, "IID('{DE89D4A9-880F-4536-9F80-CC54CCB93D43}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ApplicationName' , 'pVal' , ), 31, (31, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ApplicationName' , 'pVal' , ), 31, (31, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'MyMedia' , 'pVal' , ), 32, (32, (), [ (16393, 10, None, "IID('{14D4BE41-CBC6-4030-BA7B-C42CF18BD030}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 33, (33, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 33, (33, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ServiceProxy' , 'pVal' , ), 34, (34, (), [ (16393, 10, None, "IID('{B68682A7-55A6-437B-816F-EF7F2587E671}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'StreamingProxy' , 'pVal' , ), 35, (35, (), [ (16393, 10, None, "IID('{2896D0D0-04B3-477C-A0A2-4F89FCA8848E}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'SBSessionId' , 'pVal' , ), 36, (36, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'AnalyticsSessionId' , 'pVal' , ), 37, (37, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'DecryptPasswordForNextConnection' , ), 38, (38, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Sunshine' , 'pVal' , ), 39, (39, (), [ (16393, 10, None, "IID('{64A1F442-1541-46DF-A87E-96C1C9DB6322}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'ClosedCaption' , 'pVal' , ), 40, (40, (), [ (16393, 10, None, "IID('{B68271A5-7166-476C-9BE8-D6B9C5372C90}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'ClosedCaptionActivate' , 'pVal' , ), 41, (41, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ClosedCaptionActivate' , 'pVal' , ), 41, (41, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'FireIrCommand' , 'lCommand' , 'lExtraInfo' , 'lFlush' , 'apiReturnValue' , 
			 ), 42, (42, (), [ (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'HandleDishLoginCompletion' , 'apiReturnValue' , ), 43, (43, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SetCurrentDishReceiver' , 'receiverID' , 'apiReturnValue' , ), 44, (44, (), [ (8, 1, None, None) , 
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'SendRebootRequestToCurrentBox' , 'apiReturnValue' , ), 45, (45, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'GetSparcsResponse' , 'szFinderid' , 'uiRequestTimeOut' , ), 46, (46, (), [ (8, 1, None, None) , 
			 (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'EncryptPassword' , 'szPassword' , 'pszEncryptedPassword' , ), 47, (47, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'DecryptPassword' , 'szEncryptedPassword' , 'pszDecryptedPassword' , ), 48, (48, (), [ (8, 1, None, None) , 
			 (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionModes' , 'pVal' , ), 49, (49, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'ConnectionModes' , 'pVal' , ), 49, (49, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'PlayerInstanceID' , 'pVal' , ), 50, (50, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'ClientWanIP' , 'pVal' , ), 51, (51, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'EnableACRFeed' , ), 52, (52, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'InitACR' , 'szACRKey' , ), 53, (53, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'BindUserACR' , 'iID' , ), 54, (54, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

IStreamSettingsAX_vtables_dispatch_ = 1
IStreamSettingsAX_vtables_ = [
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 1, (1, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LANVideoRes' , 'pVal' , ), 2, (2, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LANVideoRes' , 'pVal' , ), 2, (2, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'WANVideoRes' , 'pVal' , ), 3, (3, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'WANVideoRes' , 'pVal' , ), 3, (3, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ManualVideoRes' , 'pVal' , ), 4, (4, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ManualVideoRes' , 'pVal' , ), 4, (4, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'VideoBitrate' , 'pVal' , ), 5, (5, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'VideoBitrate' , 'pVal' , ), 5, (5, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'RequiredBandWidth' , 'pVal' , ), 6, (6, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'FPS' , 'pVal' , ), 7, (7, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FPS' , 'pVal' , ), 7, (7, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'IFrameInterval' , 'pVal' , ), 8, (8, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'IFrameInterval' , 'pVal' , ), 8, (8, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'VideoSmoothness' , 'pVal' , ), 9, (9, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'VideoSmoothness' , 'pVal' , ), 9, (9, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'AudioBitRate' , 'pVal' , ), 10, (10, (), [ (16402, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AudioBitRate' , 'pVal' , ), 10, (10, (), [ (18, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Apply' , ), 11, (11, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Cancel' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RestoreToDefaults' , ), 13, (13, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DXVACapability' , 'bCapability' , ), 14, (14, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'EnableDXVA' , 'pVal' , ), 15, (15, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'EnableDXVA' , 'pVal' , ), 15, (15, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'VideoRenderer' , 'pVal' , ), 16, (16, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'VideoRenderer' , 'pVal' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IStreamingProxyInfo_vtables_dispatch_ = 1
IStreamingProxyInfo_vtables_ = [
	(( 'Username' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Username' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Password' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ServerIpAddress' , 'pVal' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ServerIpAddress' , 'pVal' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Port' , 'pVal' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Port' , 'pVal' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UseBrowserProxy' , 'pVal' , ), 5, (5, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'UseBrowserProxy' , 'pVal' , ), 5, (5, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Apply' , ), 6, (6, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

ISunshine_vtables_dispatch_ = 1
ISunshine_vtables_ = [
	(( 'Login' , 'reciverId' , 'cookie' , 'apiReturnValue' , ), 1, (1, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ChangeChannel' , 'channelNumber' , 'tvInstance' , 'apiReturnValue' , ), 2, (2, (), [ 
			 (19, 1, None, None) , (19, 1, None, None) , (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'IsCapable' , 'featureId' , 'apiReturnValue' , ), 3, (3, (), [ (19, 1, None, None) , 
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'IsBoxSunshineCapable' , 'apiReturnValue' , ), 4, (4, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetTVInfo' , 'bWakeUP' , 'apiReturnValue' , ), 5, (5, (), [ (19, 1, None, None) , 
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SetAsyncEventsSubscription' , 'subscribeAE' , 'apiReturnValue' , ), 6, (6, (), [ (19, 1, None, None) , 
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FireAsyncEventResponse' , 'strEventType' , 'strHTTPMethod' , 'strHTTPObj' , 'strPayload' , 
			 'strPassword' , 'channelNumber' , 'apiReturnValue' , ), 7, (7, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (19, 1, None, None) , 
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FireJoinTunerRequest' , 'tunerIndex' , 'svcId' , 'connId' , 'apiReturnValue' , 
			 ), 8, (8, (), [ (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SetBufferBarEventsSubscription' , 'subscribeBB' , 'apiReturnValue' , ), 9, (9, (), [ (19, 1, None, None) , 
			 (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FireLandingPageRequest' , 'apiReturnValue' , ), 10, (10, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FireDVRPlayRequest' , 'pvrID' , 'pvrAttrib' , 'playMode' , 'apiReturnValue' , 
			 ), 11, (11, (), [ (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'FireRebootRequest' , 'apiReturnValue' , ), 12, (12, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IVideoInputAX_vtables_dispatch_ = 1
IVideoInputAX_vtables_ = [
	(( 'Lineup' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ID' , 'pVal' , ), 2, (2, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Zipcode' , 'pVal' , ), 4, (4, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IsTuner' , 'pVal' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'IsCurrent' , 'pVal' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'IsEPGSupported' , 'pVal' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'IsAutoAspectSupported' , 'pVal' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 9, (9, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ChannelsCount' , 'pVal' , ), 10, (10, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetChannelAt' , 'ulIndex' , 'ptrChannelInfo' , ), 11, (11, (), [ (19, 1, None, None) , 
			 (16393, 10, None, "IID('{4192D38F-9410-41EF-AAE0-9F850B1A689F}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Lineup2' , 'pVal' , ), 12, (12, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Zipcode2' , 'pVal' , ), 13, (13, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DeviceType' , 'pVal' , ), 14, (14, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'VideoStandard' , 'pVal' , ), 15, (15, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Country' , 'pVal' , ), 16, (16, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DeviceBrand' , 'pVal' , ), 17, (17, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DeviceModel' , 'pVal' , ), 18, (18, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DeviceIRCode' , 'pVal' , ), 19, (19, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'IRDigits' , 'pVal' , ), 20, (20, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'WantsEnter' , 'pVal' , ), 21, (21, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'IRKeysCount' , 'pVal' , ), 22, (22, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'IRKeyCodes' , 'pVal' , ), 23, (23, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CurrentChannel' , 'pVal' , ), 24, (24, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'IRKeyDelay' , 'pVal' , ), 25, (25, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'IsConfigurable' , 'pVal' , ), 26, (26, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'VideoLock' , 'pVal' , ), 27, (27, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_PhysicalPortStatus' , 'pVal' , ), 28, (28, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_SoftStatus' , 'pVal' , ), 29, (29, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_SoftDisabledReason' , 'pVal' , ), 30, (30, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_HDCPStatus' , 'pVal' , ), 31, (31, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_OnPlaceShiftingStatus' , 'pVal' , ), 32, (32, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_OnPlaceShiftingDisabledReason' , 'pVal' , ), 33, (33, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_OnPlaceShiftingDisabledAssociatedInput' , 'pVal' , ), 34, (34, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'HDMI_RefreshStatus' , ), 35, (35, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'LoadInputConfig' , ), 36, (36, (), [ ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'DownloadRemoteControl' , ), 37, (37, (), [ ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
]

IVideoInputEnum_vtables_dispatch_ = 1
IVideoInputEnum_vtables_ = [
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'At' , 'ulIndex' , 'pVal' , ), 2, (2, (), [ (19, 1, None, None) , 
			 (16393, 10, None, "IID('{FFA197E7-DBE6-4D19-A9F3-D06FAB3080CC}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{F68B3100-BDA6-42FF-A765-BC6EC5415FA7}' : _ISlingPlayerEvents,
	'{05FA90E7-297F-4ED9-B041-BCF37C14CB30}' : IBoxIdentityEnum,
	'{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}' : IBoxIdentity,
	'{DCF0413B-B144-42EE-AC43-62262BEA8CA1}' : ISlingPlayer,
	'{B80CD4E6-5B02-4B6C-99BE-68F1511E9549}' : SlingPlayer,
	'{532E3283-36B3-4AA9-91F8-A6EDE9DC4209}' : IVideoInputEnum,
	'{FFA197E7-DBE6-4D19-A9F3-D06FAB3080CC}' : IVideoInputAX,
	'{4192D38F-9410-41EF-AAE0-9F850B1A689F}' : IChannel,
	'{9CEBC8CF-8907-433D-B1D7-41FE2EB1DCDB}' : IPlayerPropsAX,
	'{54B36EA5-5025-4110-9AB6-154090A89024}' : IStreamSettingsAX,
	'{626B8C4A-383B-4781-ACC2-D8B661909D43}' : IRemoteControlAX,
	'{DE5F0E99-42D7-4724-AD5F-1B46910B68E1}' : IBoxPropsAX,
	'{965C70F8-62FE-4732-A338-1B709172B2F9}' : ISQAParamsAX,
	'{5FF8AF7A-B6A3-43AB-9046-8E2D6794B5F0}' : ISlingAccountsAX,
	'{DE89D4A9-880F-4536-9F80-CC54CCB93D43}' : ISUAAX,
	'{14D4BE41-CBC6-4030-BA7B-C42CF18BD030}' : IMyMedia,
	'{B68682A7-55A6-437B-816F-EF7F2587E671}' : IServiceProxyInfo,
	'{2896D0D0-04B3-477C-A0A2-4F89FCA8848E}' : IStreamingProxyInfo,
	'{64A1F442-1541-46DF-A87E-96C1C9DB6322}' : ISunshine,
	'{B68271A5-7166-476C-9BE8-D6B9C5372C90}' : IClosedCaptionAX,
	'{00774808-0A96-45CA-A55B-B608BEE33B6E}' : BoxIdentity,
	'{EFBEECAF-71BD-4D66-A184-51B9F5252698}' : BoxIdentityEnum,
	'{3B2CBA5C-8D99-4A1D-A834-6E1543784FE4}' : PlayerPropsAX,
	'{97C4E939-FD29-4D6D-8C5F-65C99A72D128}' : VideoInputEnum,
	'{608295BB-C114-4569-9305-FE7A6792D5FC}' : VideoInputAX,
	'{59E91392-CAD0-4DB9-84A8-4A57C6AFDF1E}' : Channel,
	'{84109D64-3E5B-435B-8FA8-99314D1FAA1B}' : StreamSettingsAX,
	'{DCEA4309-3D50-4991-AA21-18BE5A9571C6}' : RemoteControlAX,
	'{DE947688-953F-4122-A9AE-1365AE038FED}' : BoxPropsAX,
	'{C95D46F1-30C7-4889-AFB8-1FF19A207AF5}' : SQAParamsAX,
	'{B8085032-9FDE-43DE-8683-C6FE8379CAE5}' : SlingAccountsAX,
	'{D79B47D1-384C-4D00-B7A3-023D4F9655B3}' : SUAAX,
	'{9B3E9F8A-72A6-4B41-9432-1B0F8D1EDD2B}' : MyMedia,
	'{F4853AF6-146C-4D56-A60D-83767F565F87}' : ServiceProxyInfo,
	'{CAF3DA44-9A95-45A7-AC4E-34CA4CC947B6}' : StreamingProxyInfo,
	'{4ACD3B99-061D-44A6-B3A0-2E516DADC83D}' : Sunshine,
	'{16E1B18E-55D9-4191-8C83-F0404CE38443}' : ClosedCaptionAX,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{05FA90E7-297F-4ED9-B041-BCF37C14CB30}' : 'IBoxIdentityEnum',
	'{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}' : 'IBoxIdentity',
	'{DCF0413B-B144-42EE-AC43-62262BEA8CA1}' : 'ISlingPlayer',
	'{532E3283-36B3-4AA9-91F8-A6EDE9DC4209}' : 'IVideoInputEnum',
	'{FFA197E7-DBE6-4D19-A9F3-D06FAB3080CC}' : 'IVideoInputAX',
	'{4192D38F-9410-41EF-AAE0-9F850B1A689F}' : 'IChannel',
	'{9CEBC8CF-8907-433D-B1D7-41FE2EB1DCDB}' : 'IPlayerPropsAX',
	'{54B36EA5-5025-4110-9AB6-154090A89024}' : 'IStreamSettingsAX',
	'{626B8C4A-383B-4781-ACC2-D8B661909D43}' : 'IRemoteControlAX',
	'{DE5F0E99-42D7-4724-AD5F-1B46910B68E1}' : 'IBoxPropsAX',
	'{965C70F8-62FE-4732-A338-1B709172B2F9}' : 'ISQAParamsAX',
	'{5FF8AF7A-B6A3-43AB-9046-8E2D6794B5F0}' : 'ISlingAccountsAX',
	'{DE89D4A9-880F-4536-9F80-CC54CCB93D43}' : 'ISUAAX',
	'{14D4BE41-CBC6-4030-BA7B-C42CF18BD030}' : 'IMyMedia',
	'{B68682A7-55A6-437B-816F-EF7F2587E671}' : 'IServiceProxyInfo',
	'{2896D0D0-04B3-477C-A0A2-4F89FCA8848E}' : 'IStreamingProxyInfo',
	'{64A1F442-1541-46DF-A87E-96C1C9DB6322}' : 'ISunshine',
	'{B68271A5-7166-476C-9BE8-D6B9C5372C90}' : 'IClosedCaptionAX',
}


NamesToIIDMap = {
	'_ISlingPlayerEvents' : '{F68B3100-BDA6-42FF-A765-BC6EC5415FA7}',
	'IBoxIdentityEnum' : '{05FA90E7-297F-4ED9-B041-BCF37C14CB30}',
	'IBoxIdentity' : '{A4CEEF08-F0EB-4459-88A7-1919CD5C425E}',
	'ISlingPlayer' : '{DCF0413B-B144-42EE-AC43-62262BEA8CA1}',
	'IVideoInputEnum' : '{532E3283-36B3-4AA9-91F8-A6EDE9DC4209}',
	'IVideoInputAX' : '{FFA197E7-DBE6-4D19-A9F3-D06FAB3080CC}',
	'IChannel' : '{4192D38F-9410-41EF-AAE0-9F850B1A689F}',
	'IPlayerPropsAX' : '{9CEBC8CF-8907-433D-B1D7-41FE2EB1DCDB}',
	'IStreamSettingsAX' : '{54B36EA5-5025-4110-9AB6-154090A89024}',
	'IRemoteControlAX' : '{626B8C4A-383B-4781-ACC2-D8B661909D43}',
	'IBoxPropsAX' : '{DE5F0E99-42D7-4724-AD5F-1B46910B68E1}',
	'ISQAParamsAX' : '{965C70F8-62FE-4732-A338-1B709172B2F9}',
	'ISlingAccountsAX' : '{5FF8AF7A-B6A3-43AB-9046-8E2D6794B5F0}',
	'ISUAAX' : '{DE89D4A9-880F-4536-9F80-CC54CCB93D43}',
	'IMyMedia' : '{14D4BE41-CBC6-4030-BA7B-C42CF18BD030}',
	'IServiceProxyInfo' : '{B68682A7-55A6-437B-816F-EF7F2587E671}',
	'IStreamingProxyInfo' : '{2896D0D0-04B3-477C-A0A2-4F89FCA8848E}',
	'ISunshine' : '{64A1F442-1541-46DF-A87E-96C1C9DB6322}',
	'IClosedCaptionAX' : '{B68271A5-7166-476C-9BE8-D6B9C5372C90}',
}


