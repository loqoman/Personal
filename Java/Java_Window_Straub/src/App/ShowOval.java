/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package App;

import edu.pcwe.uw.javaintro.shapes.Canvas;   //Anything begginning with edu.<ect.> is part of profs. own classes
import edu.pcwe.uw.javaintro.shapes.DPoint;     //Imports all the packages inside this project.
import edu.pcwe.uw.javaintro.shapes.Oval;
import edu.pcwe.uw.javaintro.shapes.Rectangle;
import edu.pcwe.uw.javaintro.shapes.Shape;
import java.awt.Color;

/**
 * Application to display an oval.
 * 
 * @author jack
 */
public class ShowOval
{
    public static void main(String[] args)
    {
        Canvas  canvas  = new Canvas();
        canvas.start();
        
        double  width   = 200;
        double  height  = 100;
        DPoint  origin  = new DPoint( 100, 100 );
        Oval    oval    = 
            new Oval( origin, Color.ORANGE, Color.BLACK, width, height );
        canvas.addShape( oval );
        
        Rectangle   rect    =
            new Rectangle( origin, null, Color.BLACK, width, height );
        canvas.addShape( rect );
        
        canvas.repaint();
    }
}
