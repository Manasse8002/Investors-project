import React from 'react'

function About() {
  let message = `There are many variations of passages of Lorem Ipsum available but the \n majority have suffered alteration in some injected humour.`;
    return (
      <section class="section-white">
 
    <div class="container">
 
      <div class="row">
      
        <div class="col-md-12 text-center">

          <h2 class="section-title">The Team </h2>

          <p class="section-subtitle">{message}</p>
              
        </div> 
            
          <div class="col-sm-6 col-md-4">

            <div class="team-item">
                
              <img src="https://demo.epic-webdesign.com/tf-pacifico/v1/images/team1a.jpg" class="team-img" alt="pic" />                   
              <h3>MANASSEH MBURU</h3>            
              <div class="team-info"><p>Head of SEO</p></div>
              <p>Manasseh is our  co-founder and has developed search strategies for a variety of clients from international brands to medium sized businesses for over five years.</p>
          
              <ul class="team-icon">
              
                <li>
                  <a href="#" class="twitter">
                  <i class="fa fa-twitter"></i>
                  </a>
                </li>
                
                <li>
                  <a href="#" class="pinterest">
                  <i class="fa fa-pinterest"></i>
                  </a>
                </li>
                
                <li>
                  <a href="#" class="facebook">
                  <i class="fa fa-facebook"></i>
                  </a>
                </li>
                
                <li>
                  <a href="#" class="dribble">
                  <i class="fa fa-dribbble"></i>
                  </a>
                </li>
                  
              </ul>
                    
                
            </div>
          </div> 
            
          <div class="col-sm-6 col-md-4">

            <div class="team-item">
            
              <img src="https://demo.epic-webdesign.com/tf-pacifico/v1/images/team2a.jpg" class="team-img" alt="pic" />
              
              <h3>NASSRA KASSIM</h3>
              
              <div class="team-info"><p>SEO Specialist</p></div>

              <p>Graduating with a degree in Spanish and English, Nassra has always loved writing and now she’s lucky enough to do it as part of her new job inside our agency.</p>
          
              <ul class="team-icon">
              
                <li><a href="#" class="twitter"><i class="fa fa-twitter"></i></a></li>
                
                <li><a href="#" class="pinterest"><i class="fa fa-pinterest"></i></a></li>
                
                <li><a href="#" class="facebook"><i class="fa fa-facebook"></i></a></li>
                
                <li><a href="#" class="dribble"><i class="fa fa-dribbble"></i></a></li>
                  
              </ul>
                
            </div>

          </div> 
          <div class="col-sm-6 col-md-4">

            <div class="team-item">
            
              <img src="https://demo.epic-webdesign.com/tf-pacifico/v1/images/team3a.jpg" class="team-img" alt="pic" />
              
              <h3>BRIGHTON FLEMMING</h3>
              
              <div class="team-info"><p>Marketing Manager</p></div>

              <p>Brighton first fell in love with digital marketing at the university. He loves to learn, and looks forward to being part of this new exciting industry for many years.</p>
          
              <ul class="team-icon">
              
                <li><a href="#" class="twitter"><i class="fa fa-twitter"></i></a></li>
                
                <li><a href="#" class="pinterest"><i class="fa fa-pinterest"></i></a></li>
                
                <li><a href="#" class="facebook"><i class="fa fa-facebook"></i></a></li>
                
                <li>
                  <a href="#" class="dribble">
                  <i class="fa fa-dribbble"></i>
                  </a>
                </li>
                  
              </ul>
                
            </div>

          </div> 
      
      </div> 
    
    </div> 

    </section>
    )

}

export default About