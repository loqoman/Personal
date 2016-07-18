/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java_2d_dsc;

import javax.swing.*;//Importing packages
import java.awt.*;


/**
 *
 * @author psp504ap001
 */
public class Rectangle_Setup extends JFrame {
  
    public Rectangle_Setup(){
            
    }
    
    
    public void paint(Graphics g){
        g.setColor(Color.RED);
        g.fillRect(100,100,20,20);
        //In the form of drawRect(w,h,x,y); 
        
    }
}
