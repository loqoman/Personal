/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package first_swing_app;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.Container;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import javax.swing.JFrame;
import javax.swing.JLabel;

/**
 *
 * @author Darwin Clark
 * 
 *
 */
public class First_Swing_App extends JFrame  {
    private static void setLookAndFeel(){ // Might as well keep this local in order to demo things easier
        try{
            UIManager.setLookAndFeel(
                    "com.sun.java.swing.plaf.nimbus.NimbusLookAndFeel"
            );
            
        }catch (Exception exc){
            System.out.println("Oh Noes! Somethig whent wrong :(");
        }
    }
    public static void main(String[] args){
        setLookAndFeel();
        Absolute_Positioning windowz = new Absolute_Positioning();
        windowz.displayGUI();
    }

}
    
