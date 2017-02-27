const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow

app.on('ready', function() {
  var pyt = require('child_process').spawn('python',[__dirname + 'flask-demo.py'])
  var openWindow = function() {
    var mainWindow = new BrowserWindow({
      width: 800,
      height: 600,
      frame: false
    })
    mainWindow.loadURL('file://' + __dirname + '/index.html')
  }
})﻿
