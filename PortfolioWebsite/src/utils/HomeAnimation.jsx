import React from 'react';
import 'css-doodle';

const HomeAnimation = () => {
    const doodleRule =`
      --circle: @p(#FFFFFF);
      --color: @p(#0099FF, #00A6FF, #00B3FF, #00C0FF, #00CCFF, 
             #00D9FF, #00E6FF, #00FFFF, 
             #00FFCC, #00FFB3, #00FFA6, #00FF99, 
             #00FF80, #00FF66, #00FF4D, #00FF33);
      :doodle {
        @grid: 30x1 / 18vmin;
        --deg: @p(-180deg, 180deg);
      }
      :container {
        perspective: 30vmin;
      }
      :after, :before {
        content: '';
        background: var(--circle); 
        @place-cell: @r(100%) @r(100%);
        @size: @r(6px);
        @shape: circle;
      }
    
      @place-cell: center;
      @size: 100%;

      box-shadow:0 0 50px var(--color);
      background: @m100(
        radial-gradient(var(--circle) 90%, transparent 0) 
        @r(-20%, 120%) @r(-20%, 100%) / 1px 1px
        no-repeat
      );

      will-change: transform, opacity;
      animation: scale-up 12s linear infinite;
      animation-delay: calc(-12s / @I * @i);

      @keyframes scale-up {
        0%, 95.01%, 100% {
          transform: translateZ(0) rotate(0);
          opacity: 0;
        }
        10% { 
          opacity: 1; 
        }
        95% {
          transform: 
            translateZ(35vmin) rotateZ(@var(--deg));
        }
      }
    `;

return (
    <div>
        <css-doodle>{doodleRule}</css-doodle>
    </div>
    );
};

export default HomeAnimation;