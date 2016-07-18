/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package first_swing_app;

import java.awt.*;
import javax.swing.*;

/**
 *
 * @author STACKOVERFLOW
 * @Stolen from stackover flow as a demonstation
 */
public class Absolute_Positioning extends JFrame {
     public void displayGUI()
    {
        JFrame frame = new JFrame("Absolute Layout Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel contentPane = new JPanel();
        contentPane.setOpaque(true);
        contentPane.setBackground(Color.WHITE);
        contentPane.setLayout(null);

        JLabel label = new JLabel(
            "This JPanel uses Absolute Positioning"
                                    , JLabel.CENTER);
        label.setSize(300, 30);
        label.setLocation(5, 5); //x = 5, y = 5 from the upper left cornor. 

        JButton button = new JButton("USELESS");
        button.setSize(100, 30); //Size(100 over and 30 down?
        button.setLocation(95, 45);//Same location as before

        contentPane.add(label);
        contentPane.add(button);

        frame.setContentPane(contentPane);
        frame.setSize(310, 125);
        frame.setLocationByPlatform(true);
        frame.setVisible(true);
    }
    public static void main(String... args)
    {
        SwingUtilities.invokeLater(new Runnable()
        {
            public void run()
            {
                new Absolute_Positioning().displayGUI();
            }
        });
    }
}
